from Sequence import Sequence
from Evolution import Evolution
from SeqTools import ToolsToWorkWithSequences

import copy

class DistanceMatrix(object):
    
    '''
    Requires a list with the name of the species
    '''

    def __init__(self, name_of_species):
        '''
        Constructor
        '''
        self.name_of_species = name_of_species
        # create the list of lists
        self.m = []
        # create for each row the column
        for r in range(len(name_of_species)):
            #
            c = [0]*len(name_of_species)
            #
            self.m.append(c)
    
    
    '''
    Add a value in position i,j (same for j,i)
    '''
    def add_value_i_j(self,i,j,d):
        self.m[i][j] = d
        self.m[j][i] = d
        
    
    '''
    Get the value at position i,j
    '''
    def get_value_i_j(self,i,j):
        return self.m[i][j]
    
    
    '''
    Set a new name at species i
    '''
    def change_name_species_i(self,i,new_name):
        self.name_of_species[i] = new_name

    
    '''
    Get the number of rows
    '''
    def n_rows(self):
        return len(self.m)
    
    
    '''
    Remove the row and column at position i
    '''
    def remove_species_i(self,i):
        #
        self.name_of_species.pop(i)
        #
        self.m.pop(i)
        #
        for j in range(len(self.m)):
            #
            self.m[j].pop(i)
                
    
    '''
    Get the name of the species
    '''            
    def get_name_of_species(self):
        return self.name_of_species
    
    
    '''
    Generate a copy of this distance matrix
    '''
    def copy(self):
        d_cop = DistanceMatrix(copy.deepcopy(self.name_of_species))
        for i in range(len(self.name_of_species)-1):
            for j in range(i+1, len(self.name_of_species)):
                d_cop.add_value_i_j(i, j, self.get_value_i_j(i,j))
        return d_cop
        

def main():
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)

    #evolve 4 sequences
    evolution.split_species_in_two("Ancestral", "Ancestral1") #from Ancestral get the first generation sequence
    evolution.split_species_in_two("Ancestral", "Ancestral2") #from Ancestral get the second generation sequence
    evolution.evolve(100)
    evolution.split_species_in_two("Ancestral1", "A1_G1_1")
    evolution.split_species_in_two("Ancestral1", "A1_G1_2")
    evolution.evolve(50)
    evolution.split_species_in_two("Ancestral2", "A2_G1_1")
    evolution.split_species_in_two("Ancestral2", "A2_G1_2")
    evolution.evolve(150)
    evolution.split_species_in_two("A1_G1_1", "SpeciesA")
    evolution.split_species_in_two("A1_G1_2", "SpeciesB")
    evolution.split_species_in_two("A2_G1_1", "SpeciesC")
    evolution.split_species_in_two("A2_G1_2", "SpeciesD")