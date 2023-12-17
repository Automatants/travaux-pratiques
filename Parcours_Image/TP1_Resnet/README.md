# TP 1: Resnet

![](https://camo.githubusercontent.com/c952d12b0086103afa5e794be1e9b0f67214ed3b8f73bcc4ce22ed0d84bed524/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4175746f6d6174616e74732f70726f6a6574732d64652d7065726d616e656e63652f6d61737465722f696d6167652d686f7374696e672f7265736e65742f736b69702e706e67)

## Description

En 2012, les chercheurs ont pu montrer l'efficacité des CNN traditionnels (couche de convolution suivie d'une fonction d'activation et d'une opération de pooling) pour classifier des images. Vous avez pu constater la puissance des CNN grâce à nos TPs. Les performances sont nettement améliorées par rapport à des réseaux classiques.

Une grande partie du succès des Réseaux de Neurones Profonds a été attribuée à ces couches supplémentaires. L'intuition derrière leur fonction est que ces couches apprennent progressivement des caractéristiques de plus en plus complexes. La première couche apprend les bords, la deuxième couche apprend les formes, la troisième couche apprend les objets, la quatrième couche apprend les yeux, et ainsi de suite.

Ainsi, la phrase "We need to go deeper" est apparue. L'idée était qu'en créant des réseaux de plus en plus profonds, on arriverait à apprendre des fonctions de plus en plus complexes. Malheureusement, cela n'a pas marché.

Un des problèmes auxquels les réseaux trop profonds doivent faire face est celui des gradients s'éteignant ou explosant :

Le problème du vanishing gradient se produit lors de la rétropropagation des gradients pendant l'apprentissage de réseaux de neurones comportant de nombreuses couches. En effet, lorsque nous utilisons des fonctions d'activation de type sigmoïde ou tangente hyperbolique, il peut se produire des situations où les gradients deviennent excessivement faibles. Étant donné que les calculs pour la mise à jour des poids se basent sur la règle de la chaîne, la présence d'un zéro dans l'une des dérivées entraîne des zéros partout.
