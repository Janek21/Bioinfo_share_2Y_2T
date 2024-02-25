from Evolution import Evolution # Importing the Sequence class from the Sequence file
from Sequence import Sequence # Importing the Evolution class from the Evolution file
from DistanceMatrix import DistanceMatrix # Importing the DistanceMatrix class from the DistanceMatrix module
from ToolsToWorkWithSequencesfinal import ToolsToWorkWithSequence # Importing it also from tools file

class DistanceBasedAlgorithms(object): #Creating a class 
    '''
    classdocs
    '''

    def __init__(self, d_matrix): #Defining a constructor for the class
        '''
        Constructor
        '''
        self.d_matrix = d_matrix #Storing the distance matrix 
    
    
    
    def NJ(self):  #Defining the NJ function
        nmatrix = self.d_matrix.copy() #Creating a copy of the distance matrix and sotring it in anew variable called nmatrix.
        while nmatrix.n_rows() > 2: #While loop for all cases where the numer of rows in the matrix is greater than 2
            nmatrix1 = nmatrix.copy()  #Coping the distance matrix in a new variable called nmatrix1
            dist = [] #Creating an empty list 

            for i in range(nmatrix1.n_rows() - 1):  # Doing a for loop through each row of the copied distance matrix, except the last one
                disti = sum(nmatrix.m[i]) #Store in a variable the sum of the postion i in the matrix
                dist.append(disti) #Appending the sum of distances 
                for j in range( i + 1, nmatrix1.n_rows()): # Loop through each column of the current row, starting from i+1
                    distj = sum(nmatrix.m[j]) #Store in a variable the sum of the postion j in the matrix
                    nvalue = ((nmatrix1.n_rows() - 2) * nmatrix1.get_value_i_j(i, j)) - disti - distj  # Update the distance matrix with the new value
                    nmatrix1.add_value_i_j(i, j, nvalue) 
            dist.append(sum(nmatrix.m[-1])) # Append the sum of distances for the last row to the list of distances
            minvalue = nmatrix1.get_value_i_j(1,0) # Get the initial minimum value from the distance matrix
            minvaluep = [1, 0] # Initialize a list to store the indices of the minimum value pair

            for j in range(nmatrix1.n_rows() - 1): #For loop through each column of the copied distance matrix, except the last one
                for i in range(j + 2, nmatrix1.n_rows()): #Another for loop thorugh rows starting at position j+2
                    if  nmatrix1.get_value_i_j(i,j) < minvalue: # Check if the actual value is less than the minimum value already found
                        minvalue = nmatrix1.get_value_i_j(i,j) #Updating the new minimum value      
                        minvaluep = [i, j] #Updating the indicies of the minimum value
            distanceij = nmatrix.get_value_i_j(minvaluep[0], minvaluep[1]) #Distance value of the minimum pair from the original distance matrix
            # Calculate the distances for the new node based on the minimum value pair 
            disti = (distanceij/2) + ( (dist[i] - dist[j]) / (2 * (nmatrix.n_rows() - 2)))
            distj = distanceij - disti #Calculating it for J
            name = "(" + nmatrix.name_of_species[minvaluep[0]] + ":" + str(disti) + ', ' + nmatrix.name_of_species[minvaluep[1]] + ":"+ str(distj) + ")"  #Construction a new name for the merged node using the names and distances of the minimum  pair.
            nmatrix.change_name_species_i(minvaluep[0], name) #Changing the name of one of the nodes

            for i in range(nmatrix.n_rows()): #For loop in the rows of the distance matrix
                ndistance = (nmatrix.get_value_i_j(i, minvaluep[0]) + nmatrix.get_value_i_j(i, minvaluep[1]) - distanceij) / 2 
                # Calculating the new distance between the current node (i) and the merged node (minvaluep[0]).
                nmatrix.add_value_i_j(i, minvaluep[0], ndistance) #Actualizing it 
            nmatrix.add_value_i_j(minvaluep[0], minvaluep[0], 0) # Setting the distance of the merged node to itself to 0.
            nmatrix.remove_species_i(minvaluep[1]) #Removing the node in position 1 from the distance matrix
        mindistance = nmatrix.get_value_i_j(0, 1)  #Calculating distances
        #Creating the final name
        nname = "(" + nmatrix.name_of_species[0] + ":" + str(0) + ', ' + nmatrix.name_of_species[1] + ":" + str(mindistance) + ")"
        nmatrix.change_name_species_i(0, nname) # Changing the name of the last node to the new.
        nmatrix.remove_species_i(1) #Removing the last specie name
        return nmatrix.get_name_of_species()[0] #Returning the last name remaining.

def main(): #Defining the main function
    species = ["A","B","C","D","E"] #Storing in a list the species
    my_distance_matrix = DistanceMatrix(species) #Calling the distance matrix
    dist = [[0,5,9,9,8],[5,0,10,10,9],[9,10,0,8,7],[9,10,8,0,3],[8,9,7,3,0]] #Setting the initial distances of the matrix


    for i in range(len(dist) - 1):  # Iterate over rows of the distance matrix
        for j in range(i + 1, len(dist)):  # Iterate over columns of the distance matrix
            d = dist[i][j]  # Get the distance value
            my_distance_matrix.add_value_i_j(i, j, d)  # Add the distance to the distance matrix

    dba = DistanceBasedAlgorithms(my_distance_matrix)  # Creating an instance of DistanceBasedAlgorithms
    print(dba.NJ())  # Printing the result of the Neighbor Joining algorithm


if __name__ == "__main__":
    main ()