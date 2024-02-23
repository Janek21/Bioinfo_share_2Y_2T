from Sequence import Sequence
from Evolution import Evolution
from ToolsToWorkWithSequence import ToolsToWorkWithSequences
from DistanceMatrix import DistanceMatrix

# define a class DistanceBasedAlgorithms that will contain the needed functions to implement NJ.
class DistanceBasedAlgorithms(object):
    '''
    classdocs
    '''

    def __init__(self, d_matrix): # define the init function that takes as argument self and a distance matrix.
        '''
        Constructor
        '''
        self.d_matrix = d_matrix # define self.d_matrix as the given d_matrix
    

    def NJ(self): # define a function NJ that takes as argument self.
        '''
        This function implements the Neighbor Joining algorithm.
        It uses a distance matrix representing the distances between the sequences.
        This function returns a phylogenic tree in Newick format.
        '''
        nmatrix = self.d_matrix.copy() # assign to nmatrix a copy of self.d_matrix to be able to modify it without affecting the original.

        while nmatrix.n_rows() > 2: # while there are more than 2 rows.
            nmatrix1 = nmatrix.copy() # create a copy of nmatrix for calculations.
            dist = [] # initialize dist as a new list to store the new distances.

            '''
            Get the distances.
            '''
            for i in range(nmatrix1.n_rows() - 1): # iterate over the rows (through -1 because we want n-1 rows). 
                disti = sum(nmatrix.m[i]) # sum the rows (i) (to calculate the distance i)
                dist.append(disti) # append the distance i to the dist list.
                for j in range(i + 1, nmatrix1.n_rows()): # iterate over the upper diagonal of the matrix.
                    distj = sum(nmatrix.m[j]) # sum the rows (j) (to calculate the distance j)
                    nvalue = ((nmatrix1.n_rows() - 2) * nmatrix1.get_value_i_j(i, j)) - disti - distj # calculate the new distance according to the positions and the distances of i and j.
                    nmatrix1.add_value_i_j(i, j, nvalue) # change the previous distance by the new one in the calculations matrix.
            dist.append(sum(nmatrix.m[-1])) # append the sum of the new distances.
            
            '''
            Get the minimum distance.
            '''
            minvalue = nmatrix1.get_value_i_j(1,0) # initialize the minimum value.
            minvaluep = [1, 0] # initialize the position of the minimum value.

            for j in range(nmatrix1.n_rows() - 1): # iterate over the rows.
                for i in range(j + 2, nmatrix1.n_rows()): # iterate over the columns (upper diagonal).
                    if  nmatrix1.get_value_i_j(i,j) < minvalue: # if the current value is smaller than the minmalue.
                        minvalue = nmatrix1.get_value_i_j(i,j) # change min value to the current value.
                        minvaluep = [i, j] # change the position of the previous min value to the current one.
            
            '''
            Get the distances between species and the new name.
            '''
            distanceij = nmatrix.get_value_i_j(minvaluep[0], minvaluep[1]) # get the total distance between the species (min distance).
            disti = (distanceij/2) + ( (dist[i] - dist[j]) / (2 * (nmatrix.n_rows() - 2))) # calculate the distance with the species i.
            distj = distanceij - disti # calculate the distance with the species j.
            name = "(" + nmatrix.name_of_species[minvaluep[0]] + ":" + str(disti) + ', ' + nmatrix.name_of_species[minvaluep[1]] + ":"+ str(distj) + ")" # get the new name (Newick format)
            nmatrix.change_name_species_i(minvaluep[0], name) # change the name in position i the matrix to the new name.

            '''
            Recalculate the distances.
            '''
            for i in range(nmatrix.n_rows()): # iterate over the rows of the matrix.
                ndistance = (nmatrix.get_value_i_j(i, minvaluep[0]) + nmatrix.get_value_i_j(i, minvaluep[1]) - distanceij) / 2 # recalculate the distance according to the new min dilaststance species being joined.
                nmatrix.add_value_i_j(i, minvaluep[0], ndistance) # update the matrix with the new distance.
            nmatrix.add_value_i_j(minvaluep[0], minvaluep[0], 0) # add a 0 in the min value[0] position in the matrix (diagonals = 0).
            nmatrix.remove_species_i(minvaluep[1]) # remove the species in position min j (already joined).
        
        '''
        Get the last species name.
        '''
        mindistance = nmatrix.get_value_i_j(0, 1) # get the distance between species 0 and 1.
        nname = "(" + nmatrix.name_of_species[0] + ":" + str(0) + ', ' + nmatrix.name_of_species[1] + ":" + str(mindistance) + ")" # create the new name.
        nmatrix.change_name_species_i(0, nname) # update the name in position 0 of the matrix to the new name.
        nmatrix.remove_species_i(1) # remove the species.

        return nmatrix.get_name_of_species()[0] # return the name of the specie remaining.
    
    
def main():
    species = ["A","B","C","D","E"] # define the species.
    my_d_matrix = DistanceMatrix(species) # create the DistanceMatrix object.
    dist = [[0,5,9,9,8],[5,0,10,10,9],[9,10,0,8,7],[9,10,8,0,3],[8,9,7,3,0]] # create the distance matrix.
    
    for i in range(len(dist)-1): # iterate over the rows.
        for j in range(i+1,len(dist)): # iterate over the columns (upper diagonal).
            d = dist[i][j] # get the distance at i, j.
            my_d_matrix.add_value_i_j(i, j, d) # add the value of d to the DistanceMatrix object at position i, j.
    
    dba = DistanceBasedAlgorithms(my_d_matrix) # create the DistanceBasedAlgorithms object.
    print('Phylogenic tree:', dba.NJ()) # print the NJ output


if __name__ == "__main__":
    main ()