from Sequence import Sequence
from Evolution import Evolution
from ToolsToWorkWithSequence import ToolsToWorkWithSequences
import copy

# create a class DistanceMatrix that will contain the necessary functions.
class DistanceMatrix(object):
    '''
    Requires a list with the name of the species
    '''

    def __init__(self, name_of_species): # define the init function that takes as arguments self and the name of the species.
        '''
        Constructor
        '''
        self.name_of_species = name_of_species # assign to self.name_of_species the name_of_species

        self.m = [] # create the list of lists (matrix)
        # create for each row the column
        for r in range(len(name_of_species)): # iterate over length of species.
            c = [0]*len(name_of_species) # create a list of the number of species.
            self.m.append(c) # append the list to the matrix (m)
    
    
    '''
    Add a value in position i,j (same for j,i)
    '''
    # define a function that modifies m adding the same value in m[i][j] than in m[j][i]
    def add_value_i_j(self,i,j,d): # the matrix is symmetric
        self.m[i][j] = d # assign d to m[i][j]
        self.m[j][i] = d # assign d to m[j][i]
        
    
    '''
    Get the value at position i,j
    '''
    # define a function that returns the value of the matrix at a given position.
    def get_value_i_j(self,i,j):
        return self.m[i][j] # return the value of m at row i, column j.
    
    
    '''
    Set a new name at species i
    '''
    # define a function that changes the name of the specie at position i.
    def change_name_species_i(self,i,new_name):
        self.name_of_species[i] = new_name # change the name of the previous specie by the new one.

    
    '''
    Get the number of rows
    '''
    # define a function that returns the number of rows.
    def n_rows(self):
        return len(self.m) # return the len of the list of lists (number of rows).
    
    
    '''
    Remove the row and column at position i
    '''
    # define a function that removes the specie at positon i.
    def remove_species_i(self,i):
        # remove the item at position i from the name of species list.
        self.name_of_species.pop(i)
        # remove the row at position i (that corresponds to the specie we want to remove)
        self.m.pop(i)
        # iterate over the length of the matrix
        for j in range(len(self.m)):
            # remove the item at position i form each row (remove column i)
            self.m[j].pop(i)
                
    
    '''
    Get the name of the species
    '''      
    # define a function that returns the name of the species.      
    def get_name_of_species(self):
        return self.name_of_species
    
    
    '''
    Generate a copy of this distance matrix
    '''
    # define a function that takes as argument self.
    def copy(self):
        # d_cop will recieve all the methods of the class
        d_cop = DistanceMatrix(copy.deepcopy(self.name_of_species))
        for i in range(len(self.name_of_species)-1): # itereate over all the species
            for j in range(i+1, len(self.name_of_species)): # iterate over all the species (starting at the species located at i+1)
                d_cop.add_value_i_j(i, j, self.get_value_i_j(i,j)) # add the value at position i, j to d_copy at position i, j
        return d_cop 
        
