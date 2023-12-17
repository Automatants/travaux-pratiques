# TP 3: Transfer Learning

## Description

En pratique, très peu de personnes entraînent des CNNs complets à partir de zéro (avec une initialisation aléatoire), car il est relativement rare de disposer d'un ensemble de données de taille suffisante. Au lieu de cela, il est courant d'utiliser des CNNs pré-entrainés sur un ensemble de données très volumineux (par exemple, ImageNet, qui contient 1,2 million d'images réparties en 1000 catégories), puis d'utiliser le CNN soit comme une initialisation, soit comme un extracteur de caractéristiques fixe pour la tâche d'intérêt. Ainsi, il y a deux moyens d'utiliser le transfert learning :

- CNN en tant qu'extracteur de caractéristiques fixes : Prenez un CNN pré-entraîné, retirez la dernière couche fully conneccted, puis traitez le reste du CNN comme un extracteur de caractéristiques fixes pour le nouveau jeu de données. Vous ajouter ensuite votre propre couche fully connected et vous entrainez seulement ça.
- Finetuner le CNN : La deuxième stratégie consiste non seulement à remplacer et ré-entraîner le classificateur sur le dessus du CNN avec le nouveau jeu de données, mais aussi à entrainer tout le réseau. Il est possible de "finetuner" toutes les couches du ConvNet, ou de conserver certaines des couches plus anciennes fixes.

Dans ce TP on va utiliser la première methode, mais la deuxième s'implémente de manière similaire

