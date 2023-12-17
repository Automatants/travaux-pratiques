# TP 3: U-Net

![](https://camo.githubusercontent.com/9b40d954ff3597eaadec75eb2fdde606687b49ecf8c2a238ebd80a94d0f4b988/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4175746f6d6174616e74732f70726f6a6574732d64652d7065726d616e656e63652f6d61737465722f696d6167652d686f7374696e672f5450345f556e65742f752d6e65742d6172636869746563747572652e706e67)

## Description
L'architecture Unet est un réseau de neurones initialement développé pour la segmentation d'images biomédicales à l'Université de Freiburg, en Allemagne. L'Unet est une sorte d'autoencodeur mais avec des connections résiduelles entre l'encodeur et le décodeur afin d'éviter la disparition du gradient et de connecter les informations extraites par l'encodeur au décodeur plus facilement. Ces connections permettent au réseasu de capturer et de propager efficacement les informations de contexte.
L'Unet est composée d'une structure encodeur-décodeur avec des connexions de saut (skip connections), lui permettant de capturer à la fois des features de haut et bas niveau.
