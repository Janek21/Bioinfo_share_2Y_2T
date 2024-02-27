from Sequence import Sequence
from Evolution import Evolution
from ToolsToWorkWithSequences import ToolsToWorkWithSequences as tools

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
	
class DistanceBasedAlgorithms(object):
	
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

	  
