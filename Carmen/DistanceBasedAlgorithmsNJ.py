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
        self.d_matrix = d_matrix    #Let the distance matrix be accessible to all the following function 
    
    
    
    
    def NJ(self):   #start the Neighbor Joining algorithm 
        nmatrix = self.d_matrix.copy()  #use the copy of our matrix to be able to moduify it without affecting the orgiinal, first degree copy 
        
        while nmatrix.n_rows() > 2:     #loop through the matrix while there are more than 2 rows to get all the species into a tree
            
            nmatrix1 = nmatrix.copy()   #make a new copy of the first copy for calculations, second degree copy 
            
            dist = []   #empyt list to store the sum of the distances 

            for i in range(nmatrix1.n_rows() - 1):  #loop through the rows -1 because we want n-1 rows 
                disti = sum(nmatrix.m[i])   #assign disti as the sum of all distances on the current row
                dist.append(disti)      #add the sum to the distance list 
                
                for j in range( i + 1, nmatrix1.n_rows()):  #loop through the remaining rows from the position after i
                    
                    distj = sum(nmatrix.m[j])   #assign distj as the sum of the disntcaes of the colmns 
                    
                    nvalue = ((nmatrix1.n_rows() - 2) * nmatrix1.get_value_i_j(i, j)) - disti - distj   #here we calculate the new distances according to the posiotn and the distances of rows and columns
                    nmatrix1.add_value_i_j(i, j, nvalue)    #add to the first degree the new distance
            dist.append(sum(nmatrix.m[-1]))     #append to the distances the sum of all the new distances 
            
            minvalue = nmatrix1.get_value_i_j(1,0)  #find the minimum values and store it
            
            minvaluep = [1, 0]      #store the indices of the minvalues 

            
            for j in range(nmatrix1.n_rows() - 1):  #loop through the rows again except the last one
                for i in range(j + 2, nmatrix1.n_rows()):   #compare 2 values ahead the remaining rows so a pair of species 
                    if  nmatrix1.get_value_i_j(i,j) < minvalue:     #check whether our previous minvalue is bigger than the position we are on
                        minvalue = nmatrix1.get_value_i_j(i,j)      #if it is then update the mivalue as the position we are on 
                        minvaluep = [i, j]      #update the new indices of the minvalue
                        
            distanceij = nmatrix.get_value_i_j(minvaluep[0], minvaluep[1])  #store the minimum distance between the 2 species
            
            disti = (distanceij/2) + ( (dist[i] - dist[j]) / (2 * (nmatrix.n_rows() - 2)))  #recalculate the distance of the rows using the  distanceij
            
            distj = distanceij - disti          #recalculate the distances of the columns using the recalculated rows and the distanceij
            
            name = "(" + nmatrix.name_of_species[minvaluep[0]] + ":" + str(disti) + ', ' + nmatrix.name_of_species[minvaluep[1]] + ":"+ str(distj) + ")"    #start storing the 2 species in newick format already 
            
            nmatrix.change_name_species_i(minvaluep[0], name)   #  change the minimium value's species with the new name  

            for i in range(nmatrix.n_rows()):   #loop through the rows normally     
                
                ndistance = (nmatrix.get_value_i_j(i, minvaluep[0]) + 
                nmatrix.get_value_i_j(i, minvaluep[1]) - distanceij) / 2    #recalculate the distances in the matrix according to the new minimium disntcaes of the species being joined 
                
                nmatrix.add_value_i_j(i, minvaluep[0], ndistance)   #add the position of the species being joined 
            nmatrix.add_value_i_j(minvaluep[0], minvaluep[0], 0)    #add the minimum values position twice and a 0 for the diagonals 
        
            nmatrix.remove_species_i(minvaluep[1])  #remove the species at the second minimum posiiont since it's already previously joined 
            
        mindistance = nmatrix.get_value_i_j(0, 1)   #find the next minimum distance 
        
        nname = "(" + nmatrix.name_of_species[0] + ":" + str(0) + ', ' + 
        
        nmatrix.name_of_species[1] + ":" + str(mindistance) + ")"   #construct a newick formatted string representing the species joined 
        
        nmatrix.change_name_species_i(0, nname)     #update the name with the newly created newick format 
            
        nmatrix.remove_species_i(1)     #remove the species to avoid redundancy since its joiend 
        
        return nmatrix.get_name_of_species()[0]     #return the name of the species 

def main():
    species = ["A","B","C","D","E"] #store the names of the different species
    my_distance_matrix = DistanceMatrix(species)    #create a distance matrix object 
    dist = [[0,5,9,9,8],[5,0,10,10,9],[9,10,0,8,7],[9,10,8,0,3],[8,9,7,3,0]]
    #represents the distances between each pair of species knowing that this is symmetric 
    
    for i in range(len(dist)-1):    #iterate through the distances except the last row 
        for j in range(i+1,len(dist)):  #loop through the remaining rows starting from the one after i 
            d = dist[i][j]  #get the distance of the posiotn we are on
            my_distance_matrix.add_value_i_j(i, j, d)   #add this distance according to the psotion we are one
    
    dba = DistanceBasedAlgorithms(my_distance_matrix)   #DistanceBasedAlgorithms object is created using the distance matrix 
    
    print(dba.NJ()) #use the dba object and apply the neighbor joining alorthim, print this 

if __name__ == "__main__":
    main ()
