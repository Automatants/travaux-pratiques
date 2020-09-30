import numpy as np
import matplotlib.pyplot as plt

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
        self.score = []

class NSGAII:
    """
    Classe permettant d'éxécuter une version boostée des algorithmes génétiques sur des problèmes de minimisation vectoriels.
    """

    def __init__(self, pop_size, pop_dim, objective_func_list, bounds_list, tournament_round = 10, mutate_rate=0.7):
        """
        Sauvegarde les hyper-paramètres de l'algorithme, et crée la population initiale.

        Paramètres :
        - pop_size (int) : Nombre d'individus de la population
        - pop_dim (int) : Taille du génome des individus
        - objective_func_list (list(function)) : Liste des fonctions objectives à minimiser
        - bounds_list (Array(Tuple(float))) : Liste des couples de bornes de chaques paramètres
        - tournament_round (int, défaut 10) : Nombre de manches dans le tournoi de sélection
        - mutate_rate (float, entre 0 et 1, défaut 0.7): Taux de mutation
        """

        # Sauvegarde des hyper-paramètres
        self.pop_dim = pop_dim
        self.pop_size = pop_size
        self.mutate_rate = mutate_rate
        self.tournament_round = tournament_round
        self.objective_func_list = objective_func_list

        # Création de la population initiale
        self.pop = [Individual([bounds_list[i][0] + (bounds_list[i][1] - bounds_list[i][0])*np.random.random() for i in range(pop_dim)]) for _ in range(pop_size)]

    def A_dom_B(self,A,B):
        """
        Renvoie True si A domine strictement B (voir le diapo pour la définition de la relation de domination).
        """
        
        # A REMPLIR
        pass

    def get_domination(self):
        """
        Assigne à chaque individu le nombre de fois où il est dominé, ainsi que la liste des individus qu'il domine.
        """
        
        # A REMPLIR
        pass
    
    def sort_in_front(self):
        """
        On construit des fronts, c'est-à-dire des groupes d'individus n'ayant pas de relation de domination entre eux.

        Conseil : Commencer par ceux qui ne sont jamais dominés.
        """

        # A REMPLIR
        pass
    
    def evaluate(self):
        """
        On évalue le génome pour les individus et on l'affecte à la liste score de celui-ci.
        """

        for elt in self.pop:
            for i in range(len(self.objective_func_list)):
                elt.score.append(self.objective_func_list[i](elt.genome))

    def get_distance_crowding(self):
        """
        Evaluation de la crowding distance une fois que le front est créé.
        """

        # A REMPLIR
        pass   

    def plot2D(self,front_num):
        """
        Affiche le front de Pareto.
        """

        plt.figure('Pareto')
        plt.clf()
        for _ in range(len(self.list_front)):
            for elt in self.list_front[front_num]:
                plt.scatter(elt.score[0],elt.score[1],color='red')

    def tournament(self): #tournoi en plusieurs rounds, on doit sortir le vainqueur uniquement
        """
        Tournoi en plusieures manches, on doit renvoyer le vainqueur uniquement.
        """

        vainqueur = None

        # A REMPLIR

        return vainqueur

    def crossover(self, parent1, parent2):
        """
        Effectue un crossover entre les deux individus.
        """

        genome = []
        for i in range(self.pop_dim):
            genome.append(parent1.genome[i] + (parent2.genome[i]-parent1.genome[i])*np.random.random()) 
        return Individual(genome)

    def mutate(self, ind):
        """
        Effectue des mutations au hasard dans le génome de l'individu.
        """

        for i in range(self.pop_dim):
            if np.random.random()<self.mutate_rate:
                ind.genome[i] = ind.genome[i] + 2/10*(np.random.random()-.5)*abs((self.pop[np.random.randint(self.pop_size)].genome[i]-self.pop[np.random.randint(self.pop_size)].genome[i])) 

    def create_offsprings(self):
        """
        On  fait un tournoi pour avoir les deux parents et on crée un enfant qu'on fait muter.

        On répète cette manip' jusqu'à avoir deux fois la population originelle.
        """

        # A REMPLIR
        pass

    def clear_score(self):
        """
        Remet les scores à 0, très important.
        """
        for i in range(len(self.pop)):
            self.pop[i].score = []


    def select_new_pop(self):
        """
        On sélectionne la nouvelle population par front décroissant, et on coupe le dernier front avec la crowding_distance pour arriver au bon nombre d'individus.
        """

        new_pop = []

        # A REMPLIR

        self.pop = new_pop


    def do_gen(self):
        """
        Calcule la génération N+1 à partir de la génération N.
        """

        plt.ion()
        self.evaluate()
        self.get_domination()
        self.sort_in_front()
        self.get_distance_crowding()
        self.create_offsprings()
        self.clear_score()
        self.evaluate()
        self.get_domination()
        self.sort_in_front()
        self.get_distance_crowding()
        self.plot2D(0)
        self.select_new_pop()
        plt.show()
        plt.pause(0.2)








