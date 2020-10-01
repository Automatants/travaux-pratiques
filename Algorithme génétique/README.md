# TP : Apprenez à construire votre propre algorithme génétique

L'objectif de ce TP est d'écrire un algorithme génétique permettant de résoudre de nombreux problèmes d'optimisations.

Pour se remettre dans le bain de Python, vous pouvez trouver des fiches avec les bases de Python, ainsi que l'utilisation de plusieurs modules très présents en Data Science sur le lien suivant : http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf (Python Basics p1 et NumPy Basics p3 vous seront utiles pour ce TP).

N’hésitez pas à poser des questions s’il y a des choses que vous ne comprenez pas ! Que ce soit aux 2As présents lors du TP ou sur le chan Automatants, nous serons ravis de répondre à vos questions.

Vous disposez de nombreux fichiers Python :

- `GA_vide.py` : Le fichier pré-rempli que vous devez compléter pour avoir votre propre algorithme génétique.
- `GA_vide_sans_classe.py` : Le même fichier qui ci-dessus, mais sans utiliser de classe. Ce fichier est donc plus simple à prendre en main et plus adapté aux débutants. Il n'y a pas de différence de fonctionnalités avec le fichier ci-dessus une fois complété.
- `NSGA_vide.py` : Un fichier pré-rempli à compléter pour créer un algorithme génétique boosté.
- `tests_functions.py` : Un receuil de fonctions de tests avec plusieurs niveaux. Elles deviennent de plus en plus compliquées, ie votre algorithme devra être de plus en plus robuste pour les résoudre.

Je vous invite à commencer par le fichier `GA_vide_sans_classe.py`, il est plus simple à prendre en main. Une fois complétée, vous pourrez essayer d'adapter votre code au format du fichier `GA_vide.py` afin de prendre en main les classes en Python, etc. Finalement, vous pourrez alors vous lancer sur le fichier `NSGA_vide.py` qui est plus compliqué, mais beaucoup plus robuste, que les deux autres.

## Sujet

### I - Algorithme génétique dans le cas unidimensionnel

Nous allons remplir le fichier `GA_vide_sans_classe.py`, car il est plus simple à prendre main. Mais les instructions qui suivent sont tout à fait applicables au fichier `GA_vide.py`.

Dans cette partie, on considérera que le génome des individus n'est qu'une seul gène. Vous pouvez donc ne pas faire d'Array pour le génome pour l'instant.

1. Commencez par créer la population initiale avec des génomes aléatoires pour les individus dans la fonction `create_population`.

2. Complétez ensuite la fonction `crossover` qui permet de croiser 2 individus afin d'en obtenir un 3ème.

3. Dans la fonction `tournament`, nous allons tout d'abord classer les individus selon leur score avec la fonction objective. Plus tard, dans le TP, vous pourrez la réécrire pour effectuer un tournoi à la place de ce classement.

La fonction suivante peut vous être utile, elle permet de trier une liste B en fonction des valeurs de la liste A.

```python
C = [x for _, x in sorted(zip(A, B), key=lambda pair: pair[0])]
```

4. Remplisssez la fonction `do_gen` qui calcule la génération suivante. C'est là que vous allez appliquez toutes les étapes (Sélection et Crossover) vues durant la formation.

Vous pouvez maintenant tester votre code sur la fonction `function_lvl_1`. Il y a un exemple sur comment utiliser votre algorithme génétique à la fin du fichier, il suffit de le lancer.

Si tout se passe bien, votre population devrait se rapprocher de 2 en abscisse et 0 en ordonnée. Vous pouvez alors continuez.

5. Introduisez des mutations dans votre population en complétant la fonction `mutate` et en rajoutez ce phénomène dans `do_gen`.

Testez votre code sur la fonction de tests `function_lvl_2`. Le minimum se trouve en -8 avec pour valeur 0.

6. Tu es sur la bonne route ! Le prochain challenge est de limiter la mutation pour ne pas sortir des bornes de la fonction `function_lvl_3` !

7. Si tu es arrivé jusque là et que ton code fonctionne, tu peux maintenant passer à la dimension 2 et plus ! Maintenant, le `genome` des individus sera sous la forme d'une Array. Il faut donc que vous adaptiez votre code pour le rendre fonctionnel à 2-dimensions, puis n-dimensions !

### II - Algorithme génétique pour des fonctions objectives vectorielles

L'algorithme que vous venez de coder fonctionne pour des fonctions objectives unidimensionnelles. Le fichier `NSGA_vide.py` vous permettra de faire un algorithme génétique pour les fonctions objectives vectorielles.

## Fonctions de test

Elles se trouvent dans le fichier `tests_functions.py`.

- `function_lvl_1` (1D) : x_min = 2 et f(x) = 0.
- `function_lvl_2` (1D) : x_min = -8 et f(x) = 0.
- `function_lvl_3` (1D, entre -500 et 500) : x_min = 416 et f(x) = -420 (environ).
- `function_lvl_4` (2D, entre -5.12 et 5.12) : x_min = [0, 0] et f(x) = 0.
- `function_lvl_5` (2D, entre -5.12 et 5.12) : x_min = [0, 0] et f(x) = 0.
- `function_lvl_6` (2D, entre 1 et 10) : x_min = [-1, 2] et f(x) = -5.
- `function_lvl_7` : Forme géométrique surprise ... (dim >= 10, toujours paire).
- `function_lvl_8` : Forme géométrique surprise ... (dim >= 20, toujours paire).
- `function_lvl_9` : Forme géométrique surprise ... (dim >= 40).
- `function_lvl_10` : Forme géométrique surprise ...(dim >= 80).
- `function_multi` (Toutes les variables entre -1.5 et 1.5) : (dim >= 6, toujours paire).

A partir de la fonction 7, les génomes des individus représentent une liste de points. C'est pour cela que la dimension de celui-ci doit toujours être paire. 


## Petits conseils

-  Commencer par un cas simple (cas à une dimension)
-  Ne pas chercher une condition d’arrêt pour l’algorithme, le faire tourner avec une boucle for
-  Le code n’est pas très long entre 100 lignes et 200 lignes maximum

Des fichiers Python vides sont donnés :  ils donnent les grandes lignes de ce qu’il faut faire, libre à vous de prendre des libertés.
