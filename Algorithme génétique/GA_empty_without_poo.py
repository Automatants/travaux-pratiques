import numpy as np
from matplotlib import pyplot as plt

def create_population(pop_cap, nb_var):
    """
    Création de la population initiale avec des traits aléatoires.

    Paramètres :
    - pop_cap (int) : Nombre d'individus de la population
    - nb_var (int) : Taille du génome des individus

    Retour :
    - (Array(Array(float))) : Un tableau d'individus où chaque chaque individu est un tableau de traits.
    """

    pop = []
    
    # A REMPLIR

    return np.array(pop)

def crossover(ind1, ind2):
    """
    On croise deux invidivus (enfin leurs génomes).
    
    Par exemple, on peut appliquer pour chaque gène, où a <= b : (a + b) / 2 + abs(b - a) * random(-1, 1)

    Paramètres :
    - ind1 (Array(float)) : Premier individu
    - ind2 (Array(float)) : Deuxième individu

    Retour :
    - (Array(float)) L'individu résultant du crossover
    """
    
    ind = np.zeros(ind1.shape) # Crée un génome vierge

    # A REMPLIR

    return ind

def mutate(ind, mutation_rate,
           ind_sample1, ind_sample2,
           bound_inf=None, bound_sup=None):
    """
    On effectue la mutation du génome de l'individu ind avec une probabilité mut_rat.

    On calcule la distance moyenne entre deux individus de la population à partir de deux individus choisis au hasard ... Pourquoi ?

    Paramètres :
    - ind (Array(float)) : Individu initial
    - mut_rate (float, entre 0 et 1) : Taux de mutation
    - ind_sample1, ind_sample2 (Array(float)) : Individus choisis au hasard dans la population 
    - bound_inf, bound_sup (float, optionnel) : Bornes pour la variation du génome

    Retour :
    - (Array(float)) L'individu initial, muté ou non
    """

    # A REMPLIR

    return ind

def tournament(pop, fitness_fnct):
    """
    Classe la population en calculant des scores ou en effectuant un tournoi.

    Paramètres :
    - pop (Array(Array(float))) : Un tableau d'individus où chaque chaque individu est un tableau de traits.
    - fitness_fnct (function): La fonction objective qui permet de calculer la performance de chaque individu.

    Retour :
    - (Array(Array(float))) : Renvoie un tableau avec le liste des individus classés ou sélectionnés.
    """

    # A REMPLIR

    return pop

def do_generation(pop, fitness_fnct):
    """
    Calcule la génération N+1 à partir de la génération N.

    Parameters :
    - pop (Array(Array(float))) : Un tableau d'individus où chaque chaque individu est un tableau de traits.
    - fitness_fnct (function): La fonction objective qui permet de calculer la performance de chaque individu.
    """

    # A REMPLIR
    pass

def plot_population(pop, fitness_fnct, start, stop):
    """
    Affiche les individus de la population actuelle et la fonction objective.

    Attention, ne fonctionne que dans le cas d'une fonction objective à une seule variable.
    """
    x = np.linspace(start, stop)
    plt.plot(x, fitness_fnct(x))
    plt.scatter(pop, fitness_fnct(np.array(pop)))
    plt.show()

def genetic_algorithm(pop_cap, nb_var, fitness_fnct, n_gen, display):
    """
    Application d'un algorithme génétique pour résoudre un problème de minimisation.

    Paramètres :
    - pop (Array(Array(float))) : Un tableau d'individus où chaque chaque individu est un tableau de traits.
    - nb_var (int) : Taille du génome des individus.
    - fitness_fnct (function): La fonction objective qui permet de calculer la performance de chaque individu.
    - n_gen (int) : Le nombre de génération à calculer.
    - display (bool) : Si True, affiche la population à chaque génération.

    Return :
    - pop : The final population after n_gen generations.
    """
    pop = create_population(pop_cap, nb_var)

    for i in range(n_gen):
        do_generation(pop, fitness_fnct)

        if display and nb_var == 1:
            plot_population(pop, fitness_fnct, -5, 5)

    return pop


