from Sequence import Sequence  											# Import Sequence class from Sequence module
from Evolution import Evolution  										# Import Evolution class from Evolution module
from ToolsToWorkWithSequences import ToolsToWorkWithSequences as tools  # Import ToolsToWorkWithSequences class from ToolsToWorkWithSequences module and alias it as 'tools'
import copy																# Import copy

class DistanceMatrix(object):											# Define Class DistanceMatrix that requires a list with the name of the species

	def __init__(self, name_of_species):								# Define constructor
		self.name_of_species = name_of_species  						# Initialize the input list 'name_of_species' as a class attribute to be used in all methods
		self.m = []  													# Create an empty list to store rows/columns for the matrix
		for r in range(len(name_of_species)):							# Create rows and columns for the matrix
			c = [0] * len(name_of_species)  							# Create columns for the matrix
			self.m.append(c)  											# Append rows with columns to create the matrix
	
	def add_value_i_j(self, i, j, d):									# Define a function to add a value in position i,j (same for j,i)
		self.m[i][j] = d  												# Set the value 'd' at row 'i', column 'j'
		self.m[j][i] = d  												# Set the value 'd' at row 'j', column 'i'
		
	
	def get_value_i_j(self, i, j):										# Define a function to get the value at position i,j
		return self.m[i][j]  											# Return the value at row 'i', column 'j'

	def change_name_species_i(self, i, new_name):						# Define a function to get a new name at species i
		self.name_of_species[i] = new_name  							# Set the new name at position 'i' in the name_of_species list
	
	def n_rows(self):													# Define a function to get the number of rows
		return len(self.m)  											# Return the number of rows in the matrix
	
	
	def remove_species_i(self, i):										# Remove the row and column at position i
		self.name_of_species.pop(i)  									# Remove the name at position 'i'
		self.m.pop(i)  													# Remove the row corresponding to the removed name
		for j in range(len(self.m)):
			self.m[j].pop(i)  											# Remove the column corresponding to the removed name
	

	def get_name_of_species(self):										# Define a function to get the list of species names
		return self.name_of_species  									# Return the list of species names
		

	def copy(self):														# Define a function to generate a copy of this distance matrix
		d_cop = DistanceMatrix(copy.deepcopy(self.name_of_species))  	# Create a copy of name_of_species and insert copies of the objects found in the original recursively
		for i in range(len(self.name_of_species) - 1):					# Iterate through the length of the name_of_species list, except for the last position
			for j in range(i + 1, len(self.name_of_species)):			# Starting from the position where the above loop is iterating through, iterate through the length of the names_of_species list
				d_cop.add_value_i_j(i, j, self.get_value_i_j(i, j))  	# Add values from the original matrix to the copied matrix
		return d_cop  													# Return the copied matrix

class DistanceBasedAlgorithms(object):									# Define Class DistanceBasedAlgorithms that requires a list with the name of the species
	
	def __init__(self, M):
		self.M = M														# Initialize the class attribute M with the provided DistanceMatrix instance

	def UPGMA(self):
		matrix = self.M													# Initialize the matrix with the provided DistanceMatrix instance
		while matrix.n_rows() > 2:										# Continue the algorithm until there are only 2 rows left in the matrix
			matrix_copy = matrix.copy()									# Create a copy of the current matrix
			distances = [sum(row) for row in matrix_copy.m[:-1]]		# Compute the sum of distances for each row, excluding the last row
			min_value, min_indices = min(								# Find the minimum value and its corresponding indices in the upper triangular part of the matrix
				(matrix_copy.get_value_i_j(i, j), [i, j])
				for j in range(matrix_copy.n_rows() - 1)
				for i in range(j + 2, matrix_copy.n_rows())
			)
			distance_ij = matrix.get_value_i_j(min_indices[0], min_indices[1]) # Get the distance value between the two clusters being merged

			dist_i = (distance_ij / 2) + (
				(distances[min_indices[0] - 1] - distances[min_indices[1] - 1])	# Compute the new distances for the merged clusters
				/ (2 * (matrix.n_rows() - 2))
			)
			dist_j = distance_ij - dist_i
			
			new_name = (												# Create a new name for the merged cluster
				"("
				+ matrix.name_of_species[min_indices[0]] + ":"
				+ str(dist_i) + ', '
				+ matrix.name_of_species[min_indices[1]] + ":"
				+ str(dist_j) + ")"
			)
			matrix.change_name_species_i(min_indices[0], new_name)
			for i in range(matrix.n_rows()):							# Update the distances in the matrix after merging clusters
				new_distance = (
					(matrix.get_value_i_j(i, min_indices[0]) +
					 matrix.get_value_i_j(i, min_indices[1]) - distance_ij)
					/ 2
				)
				matrix.add_value_i_j(i, min_indices[0], new_distance)
			matrix.add_value_i_j(min_indices[0], min_indices[0], 0)		# Set the distance to itself in the new merged cluster
			matrix.remove_species_i(min_indices[1])						# Remove one of the clusters from the matrix

		min_distance = matrix.get_value_i_j(0, 1)						# Get the final distance value between the remaining two clusters
		new_name = (													# Create a new name for the final merged cluster
			"("
			+ matrix.name_of_species[0] + ":" + str(0) + ', '
			+ matrix.name_of_species[1] + ":" + str(min_distance) + ")"
		)
		matrix.change_name_species_i(0, new_name)						# Update the name of the species at the index given by min_indices[0]
		matrix.remove_species_i(1)										# Remove one of the clusters from the matrix

		return matrix.get_name_of_species()[0] 							# Return the name of the root of the hierarchical clustering tree


def main():
	sequences = []  													# Initialize an empty list to store evolved sequences

	for times in range(4):  											# Evolve 4 sequences for testing
		sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")  # Create ancestral sequence

		transition_probability = {  									# Define a transition probability matrix for nucleotide evolution
			"A": {"G": 0.04, "C": 0.04, "T": 0.04, "A": 0.88},
			"C": {"G": 0.04, "C": 0.88, "T": 0.04, "A": 0.04},
			"G": {"G": 0.88, "C": 0.04, "T": 0.04, "A": 0.04},
			"T": {"G": 0.04, "C": 0.04, "T": 0.88, "A": 0.04}
		}

		evolution = Evolution(sequence_ancestral, transition_probability) # Create Evolution instance
		evolution.split_species_in_two("Ancestral", f"Species{times}")  # Split species into two
		evolution.evolve(1000)  										# Evolve for 1000 generations

		evolved_seq = evolution.get_sequence_species(f"Species{times}") # Get the evolved sequence
		sequences.append(evolved_seq)  									# Append evolved sequence to the list

	seq_A, seq_B, seq_C, seq_D = sequences  							# Assign evolved sequences to variables

	kk = tools()  														# Instantiate the 'tools' class

	dis_matrix = DistanceMatrix(['A', 'B', 'C', 'D'])  					# Create DistanceMatrix with species names

	for numx in range(len(dis_matrix.name_of_species)):
		for numy in range(len(dis_matrix.name_of_species)):
			d = kk.observed_pairwise_nucleotide_distance(sequences[numx], sequences[numy])  # Calculate pairwise nucleotide distance
			dis_matrix.add_value_i_j(numx, numy, d)  					# Add distance to DistanceMatrix

	matrix = dis_matrix.copy()  										# Create a copy of the distance matrix

	dba = DistanceBasedAlgorithms(matrix)  								# Instantiate DistanceBasedAlgorithms with distance matrix

	result = dba.UPGMA()  												# Perform UPGMA clustering and get the resulting hierarchical tree
	print(result)  														# Print the hierarchical tree

	
if __name__ == "__main__":												# Execute the main function if the script is run
	main()

	  
