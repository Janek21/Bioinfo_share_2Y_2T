from DistanceMatrix import DistanceMatrix  # we import distance matritix so we can us de class distancematrix to make more eficient our code
from Sequence import Sequence # we import sequence so we can us de class sequence to make more eficient our code
from Evolution import Evolution #  we import evolution so we can us de class evolution to make more eficient our code


class DistanceBasedAlgorithms(object): # we create the classe DBA to generate a new obeject an to implement the funtion UPGMA and NJ( nj is for another day.
	'''
	classdocs
	'''
	def __init__(self, d_matrix): # we put a funtion inside the class, this funtion is the constructor an it will create the onject we will us for the next funtions, the object is the matrix we will use
		'''
		Constructor
		'''
		self.d_matrix = d_matrix # we make that the matrix we give to de funtion now is visibol for all the class
		
		
	def UPGMA(self): # now we put the new funtion UPGMA, the objective of thi funtion is to merge the matrix and slowli make the matrix more small
		dm = self.d_matrix.copy() # in dm we will make a copy of the matrix so we can change the copy with out editing the origuinal matrix
		while dm.n_rows() > 1: # we create a loop that i will work until the matrix is jut one number ( this is our objectve)
			min_d = dm.get_value_i_j(0,1) # now we take the firts valiu of the matrix 
			min_i = 0 # then we tell that the i is 0
			min_j = 1 # then we tell that the j is 1
			for i in range(dm.n_rows()): # this loop is use for each row that the matrix have 
				for j in range(i+1, dm.n_rows()): # then this loop is for each colum the matrix have
					if dm.get_value_i_j(i,j) < min_d: # this if is looking if the valiu of the matrix is lower that the minimum valiu that we take before, in case is lower then... 
						min_d = dm.get_value_i_j(i,j) # we change the minimum valiu and we change min_d
						min_i = i # we stor the new position of the valiu
						min_j = j # we stor the new position of the valiu
			species_names = dm.get_name_of_species() # we store the name of all the species that are present on the matrix
			new_name = "(" + species_names[min_i] + ":" + str(min_d/2) + "," + species_names[min_j] + ":" + str(min_d/2) + ")" # then we take the name of the new speci using the values of the lowe valiu that we take from that last loop, and with that we will create a new speci
			dm.change_name_species_i(min_i, new_name) # now we will change the name of the speci and implementit in the position of the min_i
			for x in range(dm.n_rows()): # this loop is use to look all the valius of i and j that are fiferemt 
				if x != min_i and x != min_j: # if the to of them are diferent, then do this
					d_i = dm.get_value_i_j(min_i, x) # we will look the valiu of at the position of i and insertet in the variable d_i
					d_j = dm.get_value_i_j(min_j, x) # we will look the valiu of the position of j and insertet in the vatiable d_j
					new_distance = (d_i + d_j)/2 # then we will look for the new distance becaus we convine to species and now the distance are changing, for this we will take the d_i and d_j and we will sume them and divide buy 2.
					dm.add_value_i_j(min_i, x, new_distance) # now we us the funtion add valiu to change the distance is the position that is going to change, to thetermine te position we use min_i and x
			dm.remove_species_i(min_j) # now we remuve all the row that we will not need any more
		return species_names[0] # we ewrurn the spececi




def main(): # we create the funtion main, this funtion is use to look that all the class works as it should work
    species = ["A","B","C","D","E"] # firt we crate the names of the species
    my_distance_matrix = DistanceMatrix(species) # then we create an object for the class distance
    dist = [[0,5,9,9,8],[5,0,10,10,9],[9,10,0,8,7],[9,10,8,0,3],[8,9,7,3,0]] # this is the matrix with the distance of nood form each speci

    
    for i in range(len(dist)-1): # this loop is us to add the valius of the matrix to the distace matrix that we will us on the class
        for j in range(i+1,len(dist)): # it looks at inside de lists
            #d = dist[i][j] 
            my_distance_matrix.add_value_i_j(i, j, dist[i][j]) # we generate the distans matrix
    
    dba = DistanceBasedAlgorithms(my_distance_matrix) # we create a new obect, this object is from this class 
    print(dba.UPGMA())# we print the result
    #print(dba.NJ())

if __name__ == "__main__": # This line is executed when the script is run as the main program
    main() # This line calls the "main()" function we defined earlier and it starts the execution of the program
	

