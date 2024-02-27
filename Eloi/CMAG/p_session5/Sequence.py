class Sequence(object):  												# Class to represent a DNA sequence.
	def __init__(self, name, string_of_nucleotides, mutations=None): 	# Constructor
		self.name = name  												# Initialize sequence name
		if isinstance(string_of_nucleotides, str):						# Check if string_of nucleotides is a string
			self.string_of_nucleotides = list(string_of_nucleotides)	# Create a new list based on the input string_of_nucleotides
		elif isinstance(string_of_nucleotides, list):					# Check if string_of nucleotides is a list
			self.string_of_nucleotides = string_of_nucleotides			# Create a new list based on the input string_of_nucleotides
		else:															# Check if string_of_nucleotides is neither a list or a string
			raise TypeError("Use a string to initialize the sequence or a list of nucleotides") # Raise a type error to inform that the required type
			
		if mutations is None:											# If mutation is the predefined value on the constructor (None) 
			self.mutations = [0] * len(string_of_nucleotides)			# Create a new list with many 0 as nucs in string of nucs  
		else:															# If mutation is already defined
			self.mutations = mutations   								# Create new list from mutations input
	
	def nucleotide_at_position(self, position):  						# Define function to get nucleotide in defined position
		return self.string_of_nucleotides[position]						# Return the nucleotide in the defined position
 
	def sequence_length(self):  										# Define function to get length of sequence
		return len(self.mutations)										# Return length of mutation list (length of nuc sequence)
	
	def get_name(self):  												# Define function to get the name of the sequence.
		return self.name												# Return name 
   
	def copy(self, new_name):  											# Define function to make copy with different name
		return Sequence(new_name, self.string_of_nucleotides.copy(), self.mutations.copy()) # Return new instance with different name
	
	def __str__(self):  												# Define function to get a string representation of the sequence.	
		return f"{self.name} : {str(self.string_of_nucleotides)}"		# Return string with name and the string of nucs in string representation
	
	def mutate_nucleotide_at_position(self, position, nucleotide):  	# Define function to mutate nucleotide at specified position, Params: position: position to mutate, nucleotide: new nucleotide.
		if nucleotide != self.string_of_nucleotides[position]:			# If the new nucleotide is different from the current one
			self.mutations[position] = self.mutations[position] + 1		# Update mutation count 
		
		self.string_of_nucleotides[position] = nucleotide				# Replace the nucleotide at the specified position with the new nucleotide
		
	def get_number_of_mutations_at_each_position(self):  				# Get the number of mutations at each position in the sequence.
		return self.mutations											# Return the list containing mutation counts at each position		
	
def main():  															# Define main function to demonstrate the Sequence class
	
	sequence_a = Sequence("First_Species", list("ACTGACTG"))			# Create the first sequence
	sequence_b = sequence_a.copy("Second_Species")						# Create a copy of the first sequence with a different name
	
	sequence_a.mutate_nucleotide_at_position(1, "C")					# Mutate the nucleotide at position 1 in the first sequence to "C"
	sequence_b.mutate_nucleotide_at_position(2, "A")    				# Mutate the nucleotide at position 2 in the second sequence to "A"
	
	print(sequence_a)													# Print the first sequence
	print(sequence_b)													# Print the second sequence
	print("")  															# Blank line
	
	print(sequence_a.get_number_of_mutations_at_each_position())		# Print the mutation counts for each position in the first sequence
	print(sequence_b.get_number_of_mutations_at_each_position())		# Print the mutation counts for each position in the second sequence

if __name__ == "__main__":
	main()
