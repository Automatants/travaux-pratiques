import numpy as np

class indiv:
    def __init__(self,genome):
        pass

class GA:
    def __init__(self,pop_cap,nb_var,fitness_fnct):
        #Assign self variables
        #.......
        #Init pop
        #......
        pass
        
    def crossover(self,ind1,ind2,binary = False):
        pass
        #Crossing is like (b+a)/2 + abs(b-a)*rand(-1,1) for example
        
    def mutate(self,ind,mut_rate,ind_sample1,ind_sample2,bound_inf=None,bound_sup= None):
        '''Mutate ind according to the distance that exist between ind1 et ind2'''
        # choose your method
        pass
       
    def tournament(self):
        '''Ind compete in random matchup nb match is pop_cap/n_tournoi'''
        
        pass
    
            
    def do_gen(self):
        '''Do a generation'''
        # Final function
        pass