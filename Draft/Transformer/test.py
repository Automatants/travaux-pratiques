from transformers import MarianMTModel, MarianTokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Tokenizing input sentence manually
sentence = "I love oranges."
tokenized_input = tokenizer(sentence, return_tensors='pt', truncation=True)
input_ids = tokenized_input['input_ids']
attention_mask = tokenized_input['attention_mask']

# Translation inference
max_length = 64
eos_token_id = model.config.eos_token_id
decoder_start_token_id = model.config.decoder_start_token_id
decoder_input_ids = torch.tensor([[decoder_start_token_id]], dtype=torch.long)

with torch.no_grad():
	encoder_states = model.get_encoder()(input_ids, attention_mask)
	logits, _, _ = model.get_decoder()(decoder_input_ids, encoder_hidden_states=encoder_states)

# Print logits
print(logits)