import numpy as np
from matplotlib import pyplot as plt

def create_population(pop_cap, nb_var):
    """
    Create the initial population with random traits.


    Parameters :
    - pop_cap : the number of individuals
    - nb_var : the number of variables of each individual

    Return :
    - pop : Array of individuals, where individuals are an array of traits
    """
    pass

def crossover(ind1, ind2, binary = False):
    """
    Do a crossover between two individuals.

    Parameters :
    - ind1 : Array of traits of the first individual
    - ind2 : Array of traits of the second individual
    - binary : ???

    Return :
    - ind : Array of traits of the crossover between the two
    """
    pass

def mutate(ind, mutation_rate, ind_sample1, ind_sample2, bound_inf=None, bound_sup=None):
    """
    Random chance to generate a new mutation.

    Parameters :
    - ind : Array of traits of the individual to mutate
    - mutation_rate : Mutation rate
    - ind_sample1, ind_sample2 : Array of traits of individuals picked from the population to estimate the average space between two individuals
    - bound_inf, bound_sup : Limits the mutation range
    """
    pass

def tournament(pop, fitness_fnct):
    """
    Rank your population by calculating a score or by doing a tournament.

    Parameters :
    - pop : Array of individuals, where individuals are an array of traits
    - fitness_fnct : A fitness function to evaluate the performance of a given individual
    """
    pass

def do_generation(pop, fitness_fnct):
    """
    Calculate generation N+1. given generation N

    Parameters :
    - pop : Array of individuals, where individuals are an array of traits
    - fitness_fnct : A fitness function to evaluate the performance of a given individual
    """
    pass

def plot_population(pop, fitness_fnct, start, stop):
    """
    Plot the current population against the fitness function.
    """
    x = np.linspace(start, stop)
    plt.plot(x, fitness_fnct(x))
    plt.scatter(pop, fitness_fnct(np.array(pop)))
    plt.show()

def genetic_algorithm(pop_cap, nb_var, fitness_fnct, n_gen, display):
    """
    Apply a genetic algorithm to solve a problem.

    Parameters :
    - pop_cap : the number of individuals
    - nb_var : the number of variables of each individual
    - fitness_fnct : A fitness function to evaluate the performance of a given individual
    - n_gen : the number of generation to calculate

    Return :
    - pop : The final population after n_gen generations.
    """
    pop = create_population(pop_cap, nb_var)

    for i in range(n_gen):
        do_generation(pop, fitness_fnct)

        if display and nb_var == 1:
            plot_population(pop, fitness_fnct, -5, 5)

    return pop


