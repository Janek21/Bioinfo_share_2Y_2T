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
		
	def UPGMA(self, m):
		print()
		print(self.name_of_species)
		length = len(self.m)
		if length <= 0:
			return self.m
		min_val = min(min(self.m[row][val] if val != row else float('+inf') for val in range(length)) for row in range(length))
		print(min_val)
		
		for posx in range(length):
			for posy in range(length):
				if self.m[posx][posy] == min_val:
					print(f'namex: {self.name_of_species[posx]} namey: {self.name_of_species[posy]}')
					print(f'posy: {posy} posx: {posx}')
					matrix_copy = self.copy()
					# Perform operations on the copied matrix
					self.change_name_species_i(posx, f'({self.name_of_species[posx]}:{self.name_of_species[posy]})')
					self.add_value_i_j(posx, posy, (matrix_copy.m[posx][posx] + matrix_copy.m[posx][posy]) / 2)
					self.remove_species_i(posy)

					# Print statements for debugging
					for row in matrix_copy.m:
						print(row)
					for row in self.m:
						print(row)

					return self.UPGMA(self.m)
		return self.m			


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
		

# Define main function
def main():
	sequences = []

	for times in range(4):
		sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
		transition_probability = {
			"A": {"G": 0.04, "C": 0.04, "T": 0.04, "A": 0.88},
			"C": {"G": 0.04, "C": 0.88, "T": 0.04, "A": 0.04},
			"G": {"G": 0.88, "C": 0.04, "T": 0.04, "A": 0.04},
			"T": {"G": 0.04, "C": 0.04, "T": 0.88, "A": 0.04}
		}

		evolution = Evolution(sequence_ancestral, transition_probability)
		evolution.split_species_in_two("Ancestral", f"Species{times}")
		evolution.evolve(1000)

		evolved_seq = evolution.get_sequence_species(f"Species{times}")

		sequences.append(evolved_seq)

	# Now, sequences list contains the evolved sequences for each iteration
	seq_A, seq_B, seq_C, seq_D = sequences
	# Instantiate the 'tools' class
	kk = tools()

	# Create a DistanceMatrix using the evolved sequences
	dis_matrix = DistanceMatrix(['A', 'B', 'C', 'D'])

	# Loop through the sequences and compute the observed pairwise nucleotide distances
	for numx in range(len(dis_matrix.name_of_species)):
		for numy in range(len(dis_matrix.name_of_species)):
			d = kk.observed_pairwise_nucleotide_distance(sequences[numx],sequences[numy])
			dis_matrix.add_value_i_j(numx, numy, d)

	# Print the resulting distance matrix
	for row in dis_matrix.m:
		print(row)
	result = dis_matrix.UPGMA(dis_matrix.m)
	for row in result:
		print(row)
		
	
	

	

# Execute the main function if the script is run
if __name__ == "__main__":
	main()

	  
