import torchtext
import torch
import math
import torch.nn as nn

X_train = ["I like oranges.", "I don't like oranges.", "I like apples.", "I like bananas.", "I don't like pineapples and oranges."]
Y_train = ["J'aime les oranges.", "Je n'aime pas les oranges.", "J'aime les pommes.", "J'aime les bananes.", "Je n'aime pas les ananas et les oranges."]

X_test = ["I like pineapples.", "I don't like pineapples."]


# add <start> and <end> tokens
X_train = ["<start> " + x + " <end>" for x in X_train]
Y_train = ["<start> " + y + " <end>" for y in Y_train]

X_test = ["<start> " + x + " <end>" for x in X_test]


tokenizer = torchtext.data.utils.get_tokenizer('basic_english')
X_train = [tokenizer(x) for x in X_train]
Y_train = [tokenizer(y) for y in Y_train]

X_test = [tokenizer(x) for x in X_test]

# vocab
vocab = torchtext.vocab.build_vocab_from_iterator(X_train + Y_train, specials=["<pad>", "<unk>"])
vocab.set_default_index(vocab["<unk>"])

# padding
X_train = [torch.tensor([vocab[token] for token in x]) for x in X_train]
Y_train = [torch.tensor([vocab[token] for token in y]) for y in Y_train]

X_test = [torch.tensor([vocab[token] for token in x]) for x in X_test]

# padding
X_train = torch.nn.utils.rnn.pad_sequence(X_train, batch_first=True, padding_value=vocab["<pad>"])
Y_train = torch.nn.utils.rnn.pad_sequence(Y_train, batch_first=True, padding_value=vocab["<pad>"])

X_test = torch.nn.utils.rnn.pad_sequence(X_test, batch_first=True, padding_value=vocab["<pad>"])

# key padding mask
X_train_key_padding_mask = (X_train == vocab["<pad>"]).bool()
Y_train_key_padding_mask = (Y_train == vocab["<pad>"]).bool()

X_test_key_padding_mask = (X_test == vocab["<pad>"]).bool()


class PositionalEncoding(nn.Module):
	def __init__(self, d_model, dropout=0.1, max_len=5000):
		super().__init__()
		self.dropout = nn.Dropout(p=dropout)

		pe = torch.zeros(max_len, d_model)
		position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1) # (max_len, 1)
		div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)) # (d_model / 2)
		pe[:, 0::2] = torch.sin(position * div_term) # (max_len, d_model / 2)
		pe[:, 1::2] = torch.cos(position * div_term) # (max_len, d_model / 2)
		pe = pe.unsqueeze(0) # (1, max_len, d_model)
		self.register_buffer('pe', pe)

	def forward(self, x):
		"""
		x: (batch_size, seq_len, d_model)
		"""
		x = x + self.pe[:, :x.size(1)] # (batch_size, seq_len, d_model)
		return x


import math
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class TransformerModel(nn.Module):
	def __init__(self, vocab_size, d_model, nhead, nhid, nlayers, dropout=0.5):
		super(TransformerModel, self).__init__()
		self.model_type = 'Transformer'
		self.pos_encoder = PositionalEncoding(d_model, dropout)
		encoder_layers = nn.TransformerEncoderLayer(d_model, nhead, nhid, dropout, batch_first=True)
		decoder_layers = nn.TransformerDecoderLayer(d_model, nhead, nhid, dropout, batch_first=True)
		self.transformer_encoder = nn.TransformerEncoder(encoder_layers, nlayers)
		self.transformer_decoder = nn.TransformerDecoder(decoder_layers, nlayers)
		self.encoder = nn.Embedding(vocab_size, d_model)
		self.d_model = d_model
		self.decoder = nn.Linear(d_model, vocab_size)

		# causal mask
		causal_mask = torch.triu(torch.ones(100, 100), diagonal=1).bool()
		self.register_buffer('causal_mask', causal_mask)

	def forward(self, src, tgt, src_mask, tgt_mask):
		src = self.encoder(src)
		src = self.pos_encoder(src)
		tgt = self.encoder(tgt)
		output = self.transformer_encoder(src, src_key_padding_mask=src_mask)
		output = self.transformer_decoder(tgt, output, tgt_mask=self.causal_mask[:tgt.size(1), :tgt.size(1)], tgt_key_padding_mask=tgt_mask, memory_key_padding_mask=src_mask)
		output = self.decoder(output)
		return output


# Hyperparameters
d_model = 128
nhead = 4
nhid = 512
nlayers = 3
dropout = 0.1
learning_rate = 0.0001
batch_size = 64
epochs = 100

# Model, Loss function, and Optimizer
model = TransformerModel(len(vocab), d_model, nhead, nhid, nlayers, dropout).to("cuda")
criterion = nn.CrossEntropyLoss(reduction='none')
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


X_train = X_train.to("cuda")
Y_train = Y_train.to("cuda")
tgt = Y_train[:, :-1]
ground_truth = Y_train[:, 1:]

X_train_key_padding_mask = X_train_key_padding_mask.to("cuda")
Y_train_key_padding_mask = Y_train_key_padding_mask.to("cuda")

tgt_key_padding_mask = Y_train_key_padding_mask[:, :-1]
ground_truth_key_padding_mask = Y_train_key_padding_mask[:, 1:]


for epoch in range(epochs):
	total_loss = 0

	optimizer.zero_grad()
	output = model(X_train, tgt, X_train_key_padding_mask, tgt_key_padding_mask)
	loss = criterion(output.transpose(1, 2), ground_truth)
	loss = (loss * (1 - ground_truth_key_padding_mask.float())).sum() / ground_truth_key_padding_mask.sum()
	loss.backward()
	optimizer.step()

	print("Epoch: {}, Loss: {}".format(epoch, loss.item()))


# Test
X_test = X_test.to("cuda")
X_test_key_padding_mask = X_test_key_padding_mask.to("cuda")
model.eval()
for i in range(len(X_test)):
	cur_pred = ["<start>"]
	while cur_pred[-1] != "<end>":
		cur_input = torch.tensor([[vocab[token] for token in cur_pred]]).to("cuda")
		cur_input_key_padding_mask = torch.zeros((1, len(cur_pred))).bool().to("cuda")
		src_padding_mask = torch.zeros((1, len(X_test[i]))).bool().to("cuda")
		cur_output = model(X_test[i].unsqueeze(0), cur_input, src_padding_mask, cur_input_key_padding_mask)
		cur_pred.append(vocab.get_itos()[cur_output[0, -1].argmax().item()])

	print(" ".join(cur_pred[1:-1]))