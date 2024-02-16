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
        self.name_of_species = name_of_species #defines the input list name_of_species to be able to be used in all methods
        # create the list of lists
        self.m = []
        # create for each row the column
        for r in range(len(name_of_species)):
            #create the columns for m
            c = [0]*len(name_of_species)
            #append the rows with columns
            self.m.append(c)
    
    
    '''
    Add a value in position i,j (same for j,i)
    '''
    def add_value_i_j(self,i,j,d):#given positions i j in the matrix and value d
        self.m[i][j] = d #set d in row i, column j
        self.m[j][i] = d #set d in row j, column i
        
    
    '''
    Get the value at position i,j
    '''
    def get_value_i_j(self,i,j): #given position i, j
        return self.m[i][j] #return value at row i, column j
    
    
    '''
    Set a new name at species i
    '''
    def change_name_species_i(self,i,new_name): #for position i and a name
        self.name_of_species[i] = new_name #in name_of_species(input list) set name in position i to a new name
    
    '''
    Get the number of rows
    '''
    def n_rows(self): #return number of rows in the matrix
        return len(self.m)
    
    
    '''
    Remove the row and column at position i
    '''
    def remove_species_i(self,i): #for a position i
        #eliminate the name in position i
        self.name_of_species.pop(i)
        #eliminate the row of the matrix that corresponds to the name you just erased
        self.m.pop(i) 
        #eliminate the column of the matrix that corresponds to the name you just removed
        for j in range(len(self.m)):
            
            self.m[j].pop(i)
                
    
    '''
    Get the name of the species
    '''
    def get_name_of_species(self): #returns the list of species names
        return self.name_of_species
    
    
    '''
    Generate a copy of this distance matrix
    '''
    def copy(self):

        #Creates a copy of name_of_species and inserts copies of the objects found in the original recursively, then it definesa new DistanceMatrix object with it and names it d_cop
        d_cop = DistanceMatrix(copy.deepcopy(self.name_of_species)) 

        #iterate through the length of the name of species list, except for the last position
        for i in range(len(self.name_of_species)-1):
            #starting from the position where the above loop is iterating through, iterate through the length of the names of species list
            for j in range(i+1, len(self.name_of_species)):
                #use the previously defined add_value_i_j and get_value_i_j functions to add the value on position i j of our original matrix into position i j of d_cop
                d_cop.add_value_i_j(i, j, self.get_value_i_j(i,j))

        return d_cop #return the copied matrix


def main():
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)

    #evolve 4 sequences
    evolution.split_species_in_two("Ancestral", "Ancestral1") #from Ancestral get the first generation sequence
    evolution.split_species_in_two("Ancestral", "Ancestral2") #from Ancestral get the second generation sequence
    evolution.evolve(100) #100 generations pass
    evolution.split_species_in_two("Ancestral1", "A1_G1_1") #at 100 generations from start ancestral 1 develops in 2 sequences (generation 1, sequences 1 and 2)
    evolution.split_species_in_two("Ancestral1", "A1_G1_2")
    evolution.evolve(50) #50 more generations pass
    evolution.split_species_in_two("Ancestral2", "A2_G1_1") ##at 150 generations from start ancestral 2 develops in 2 sequences (generation 1, sequences 1 and 2)
    evolution.split_species_in_two("Ancestral2", "A2_G1_2")
    evolution.evolve(150) #150 more generatins pass
    evolution.split_species_in_two("A1_G1_1", "SpeciesA") #at 100 and 150 generations from start, ancestral 1 and 2 have developed 2 sequences each, known as generation 1 
    evolution.split_species_in_two("A1_G1_2", "SpeciesB") #Now, 300 generations from start, each sequence from generation 1 has evolved into another sequence
    evolution.split_species_in_two("A2_G1_1", "SpeciesC")
    evolution.split_species_in_two("A2_G1_2", "SpeciesD")

    species_names=evolution.get_list_of_species_name() #get the name of all species and define species as that list

    dist_ab=DistanceMatrix(species_names)#use the list of names of species as input for the DistanceMatrix class
    

if __name__ == "__main__":
    main ()