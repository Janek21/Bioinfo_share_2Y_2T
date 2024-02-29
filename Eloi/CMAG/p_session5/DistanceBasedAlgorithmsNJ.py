from Evolution import Evolution  										# Import the Evolution class
from Sequence import Sequence  											# Import the Sequence class
from DistanceMatrix import DistanceMatrix  								# Import the DistanceMatrix class
from ToolsToWorkWithSequences import ToolsToWorkWithSequences  			# Import the ToolsToWorkWithSequences class


class DistanceBasedAlgorithms(object):  								# Define a class for distance-based phylogenetic algorithms
	def __init__(self, d_matrix):  										# Constructor for the DistanceBasedAlgorithms class.
		self.d_matrix = d_matrix  										# Parameters: - d_matrix: DistanceMatrix object representing the pairwise distances between species.

	def NJ(self):  														# Neighbor-Joining (NJ) algorithm for constructing a phylogenetic tree based on distance matrix.
		nmatrix = self.d_matrix.copy()  								# Copy the distance matrix to avoid modifying the original

		while nmatrix.n_rows() > 2:  									# Loop until the number of rows in the distance matrix is reduced to 2
			nmatrix1 = nmatrix.copy()  									# Create a copy of the distance matrix
			dist = []  													# Initialize a list to store sum of distances for each row

			for i in range(nmatrix1.n_rows() - 1):  					# Iterate over each row to calculate the sum of distances
				disti = sum(nmatrix.m[i]) 							 	# Sum the distances for the current row
				dist.append(disti)  									# Append the sum to the 'dist' list
				
				for j in range(i + 1, nmatrix1.n_rows()):  				# Iterate over the upper triangular part of the distance matrix
					distj = sum(nmatrix.m[j])  							# Sum the distances for the current column
					nvalue = ((nmatrix1.n_rows() - 2) * nmatrix1.get_value_i_j(i, j)) - disti - distj  # Calculate the updated distance value
					nmatrix1.add_value_i_j(i, j, nvalue)  				# Update the distance matrix with the new value

			
			dist.append(sum(nmatrix.m[-1]))  							# Append the sum of distances for the last row

			minvalue = nmatrix1.get_value_i_j(1, 0)  					# Find the minimum value in the updated distance matrix
			minvaluep = [1, 0]  										# Initialize indices for the minimum value position

			for j in range(nmatrix1.n_rows() - 1):  					# Iterate over the upper triangular part of the updated distance matrix
				for i in range(j + 2, nmatrix1.n_rows()):  				# Continue iterating over the remaining elements
					if nmatrix1.get_value_i_j(i, j) < minvalue:  		# Check if the current value is smaller than the current minimum
						minvalue = nmatrix1.get_value_i_j(i, j)  		# Update the minimum value
						minvaluep = [i, j]  							# Update the position of the minimum value

			distanceij = nmatrix.get_value_i_j(minvaluep[0], minvaluep[1])  # Get the distance between the selected species
			disti = (distanceij / 2) + ((dist[i] - dist[j]) / (2 * (nmatrix.n_rows() - 2)))  # Calculate the new distance for the first species
			distj = distanceij - disti  								# Calculate the new distance for the second species
			name = "(" + nmatrix.name_of_species[minvaluep[0]] + ":" + str(disti) + ', ' + nmatrix.name_of_species[minvaluep[1]] + ":" + str(distj) + ")" 
			nmatrix.change_name_species_i(minvaluep[0], name)  			# Update the name of the selected species

			for i in range(nmatrix.n_rows()):  							# Update distances in the distance matrix
				ndistance = (nmatrix.get_value_i_j(i, minvaluep[0]) + nmatrix.get_value_i_j(i, minvaluep[1]) - distanceij) / 2  # Calculate the new distance for each species in the updated matrix
				nmatrix.add_value_i_j(i, minvaluep[0], ndistance)  		# Update the distance for the first species
			nmatrix.add_value_i_j(minvaluep[0], minvaluep[0], 0)  		# Set the distance to itself as 0
			nmatrix.remove_species_i(minvaluep[1])  					# Remove the row/column of the joined species


		mindistance = nmatrix.get_value_i_j(0, 1)  						# Get the final distance between the last two species
		nname = "(" + nmatrix.name_of_species[0] + ":" + str(0) + ', ' + nmatrix.name_of_species[1] + ":" + str(mindistance) + ")" # Create the new name for the remaining species in the final tree
		nmatrix.change_name_species_i(0, nname)  						# Update the name of the remaining species
		nmatrix.remove_species_i(1)  									# Remove the second remaining species
		return nmatrix.get_name_of_species()[0]  						# Return the name of the final joined species

def main():  															# Main function
	species = ["A", "B", "C", "D", "E"]  								# Example species
	my_distance_matrix = DistanceMatrix(species)  						# Create a distance matrix for the example species
	dist = [[0, 5, 9, 9, 8], [5, 0, 10, 10, 9], [9, 10, 0, 8, 7], [9, 10, 8, 0, 3], [8, 9, 7, 3, 0]]  # Example distance matrix

	for i in range(len(dist) - 1):  									# Iterate over rows
		for j in range(i + 1, len(dist)): 								# Iterate over columns, skipping already populated values
			d = dist[i][j]  											# Get the distance value
			my_distance_matrix.add_value_i_j(i, j, d)  					# Add the distance value to the matrix


	dba = DistanceBasedAlgorithms(my_distance_matrix)  					# Create an instance of DistanceBasedAlgorithms and apply the Neighbor-Joining algorithm
	print(dba.NJ())  													# Print the final phylogenetic tree

if __name__ == "__main__":  											# Execute the script
	main()
