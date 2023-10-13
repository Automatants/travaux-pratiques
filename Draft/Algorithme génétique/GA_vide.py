import numpy as np
from matplotlib import pyplot as plt

import importlib
tests_functions = importlib.import_module('tests_functions')

class Individual:
    """
    Un individu de la population.

    Toutes les informations le concernant se trouvent l'attribut `genome`
    """

    def __init__(self, genome):
        """
        Affecte à chaque individu son génome et ses autres caractéristiques

        Paramètres :
        - genome (Array(float)) : Tableau de flottants où chaque flottant représente un "gène"
        """

        self.genome = genome

class GA:
    """
    Classe permettant d'éxécuter un algorithme génétique sur un problème d'optimisation.
    """

    def __init__(self, pop_cap, nb_var, fitness_fnct):
        """
        Sauvegarde les hyper-paramètres de l'algorithme, et crée la population initiale.

        Paramètres :
        - pop_cap (int) : Nombre d'individus de la population
        - nb_var (int) : Taille du génome des individus
        - fitness_fnct (function) : Fonction objective à minimiser
        """

        # Sauvegarde des hyper-paramètres
        self.pop_cap      = pop_cap
        self.nb_var       = nb_var
        self.fitness_fnct = fitness_fnct

        # Création de la population initiale

        # A REMPLIR
        
    def crossover(self, ind1, ind2):
        """
        On croise deux invidivus (enfin leurs génomes).

        Par exemple, on peut appliquer pour chaque gène, où a <= b : (a + b) / 2 + abs(b - a) * random(-1, 1)

        Paramètres :
        - ind1 (Individual) : Premier individu
        - ind2 (Invididual) : Deuxième individu

        Retour :
        - (Individual) L'individu résultant du crossover
        """

        genome = [0] * self.nb_var


        # A REMPLIR

        ind = Individual(genome)
        return ind
        
    def mutate(self, ind, mut_rate,
               ind_sample1, ind_sample2,
               bound_inf=None, bound_sup= None):
        """
        On effectue la mutation du génome de l'individu ind avec une probabilité mut_rat.

        On calcule la distance moyenne entre deux individus de la population à partir de deux individus choisis au hasard ... Pourquoi ?

        Paramètres :
        - ind (Individual) : Individu initial
        - mut_rate (float, entre 0 et 1) : Taux de mutation
        - ind_sample1, ind_sample2 (Individual) : Individus choisis au hasard dans la population 
        - bound_inf, bound_sup (float, optionnel) : Bornes pour la variation du génome

        Retour :
        - (Individual) L'individu initial, muté ou non
        """

        # A REMPLIR

        return ind 


       
    def tournament(self):
        """
        Effectue un tournoi entre les individus de la population.
        Alternativement, peut classer les individus selon leur performance.
        """

        # A REMPLIR
        
        pass
    
            
    def do_gen(self):
        """
        Calcule la génération N+1 à partir de la génération N.
        """

        # A REMPLIR
        pass

def plot_population(pop, fitness_fnct, start=-5, stop=5):
    """
    Affiche les individus de la population actuelle et la fonction objective.

    Attention, ne fonctionne que dans le cas d'une fonction objective à une seule variable.
    """

    x = np.linspace(start, stop)
    plt.plot(x, fitness_fnct(x))
    plt.scatter([ind.genome for ind in pop], fitness_fnct(np.array([ind.genome for ind in pop])))
    plt.show()

fitness_fnct = tests_functions.function_lvl_1
algo = GA(10, 1, fitness_fnct)
for i in range(5):
    algo.do_gen()
    plot_population(algo.pop, fitness_fnct, -3, 7)
