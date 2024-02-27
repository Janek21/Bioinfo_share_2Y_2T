from Evolution import Evolution
from Sequence import Sequence
from DistanceMatrix import DistanceMatrix
from ToolsToWorkWithSequences import ToolsToWorkWithSequences

class DistanceBasedAlgorithms(object):
    '''
    classdocs
    '''

    def __init__(self, d_matrix):
        '''
        Constructor
        '''
        self.d_matrix = d_matrix
    
    
    
    
    def NJ(self):
        nmatrix = self.d_matrix.copy()
        while nmatrix.n_rows() > 2:
            nmatrix1 = nmatrix.copy() 
            dist = [] 

            for i in range(nmatrix1.n_rows() - 1):
                disti = sum(nmatrix.m[i])
                dist.append(disti)
                for j in range( i + 1, nmatrix1.n_rows()):
                    distj = sum(nmatrix.m[j]) 
                    nvalue = ((nmatrix1.n_rows() - 2) * nmatrix1.get_value_i_j(i, j)) - disti - distj 
                    nmatrix1.add_value_i_j(i, j, nvalue) 
            dist.append(sum(nmatrix.m[-1])) 
            minvalue = nmatrix1.get_value_i_j(1,0) 
            minvaluep = [1, 0] 

            for j in range(nmatrix1.n_rows() - 1):
                for i in range(j + 2, nmatrix1.n_rows()):
                    if  nmatrix1.get_value_i_j(i,j) < minvalue: 
                        minvalue = nmatrix1.get_value_i_j(i,j) 
                        minvaluep = [i, j]
            distanceij = nmatrix.get_value_i_j(minvaluep[0], minvaluep[1]) 
            disti = (distanceij/2) + ( (dist[i] - dist[j]) / (2 * (nmatrix.n_rows() - 2)))
            distj = distanceij - disti
            name = "(" + nmatrix.name_of_species[minvaluep[0]] + ":" + str(disti) + ', ' + nmatrix.name_of_species[minvaluep[1]] + ":"+ str(distj) + ")" 
            nmatrix.change_name_species_i(minvaluep[0], name) 

            for i in range(nmatrix.n_rows()): 
                ndistance = (nmatrix.get_value_i_j(i, minvaluep[0]) + nmatrix.get_value_i_j(i, minvaluep[1]) - distanceij) / 2 
                nmatrix.add_value_i_j(i, minvaluep[0], ndistance) 
            nmatrix.add_value_i_j(minvaluep[0], minvaluep[0], 0) 
            nmatrix.remove_species_i(minvaluep[1]) 
        mindistance = nmatrix.get_value_i_j(0, 1) 
        nname = "(" + nmatrix.name_of_species[0] + ":" + str(0) + ', ' + nmatrix.name_of_species[1] + ":" + str(mindistance) + ")"
        nmatrix.change_name_species_i(0, nname) 
        nmatrix.remove_species_i(1) 
        return nmatrix.get_name_of_species()[0] 

def main():
    species = ["A","B","C","D","E"]
    my_distance_matrix = DistanceMatrix(species)
    dist = [[0,5,9,9,8],[5,0,10,10,9],[9,10,0,8,7],[9,10,8,0,3],[8,9,7,3,0]]

    
    for i in range(len(dist)-1):
        for j in range(i+1,len(dist)):
            d = dist[i][j]
            my_distance_matrix.add_value_i_j(i, j, d)
    
    dba = DistanceBasedAlgorithms(my_distance_matrix)    
    print(dba.NJ())

if __name__ == "__main__":
    main ()
