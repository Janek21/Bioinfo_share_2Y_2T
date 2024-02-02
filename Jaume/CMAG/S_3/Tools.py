# Creation of the class
class ToolsToWorkWithSeq(object):

	# Initialiting the class
	def __init__(self):
		pass
	
	# Defining a function that will get the percentage of each nucleotide in a sequence (as string or list)
	def nucleotide_statistics(self, seq):

		# Defining some variables
		n = len(seq) # Getting the length
		stats = {'A': 0, 'C': 0, 'T': 0, 'G': 0} # Creating the dictionary that will have te count of each nucleotide

		# Iteration through each item of the variable seq (list or string)
		for i in seq:

			'''
			Updating the count of the current nucleotide in the 'stats' dictionary by its
			proportion in the sequence, multiplied by 100 to get a percentage instead of a frequence.
			'''
			stats[i] += (1 / n) * 100
		
		return stats # Getting the result
	
	def observed_pairwise_nucleotide_distance(self, seq1, seq2):

		'''
		To handle a possible case in which the length of the sequences are different

		1- Checking which sequence is shorter
		2- Getting the length of the shorter sequence

		We will use the stop variable to avoid out of range errors by not calling the index when out of range
		'''
		if seq2 > seq1:
			stop = len(seq1)
		
		else:
			stop = len(seq2)
		
		# Creation of the variable result
		result = 0

		# Loop to iterate through the longest sequence
		for i in range(stop):
			
			# If the iteration is in range, checking if the nucleotides are the same or not
			if seq1[i] != seq2[i]:

				# Adding up 1 if the nucleotides are different
				result += 1
			
			# If the iteration is in range and the nucleotides are the same, continuing
			else:
				pass
		
		# Having in account the length difference
		result += abs(len(seq1) - len(seq2))

		return result # Returning the output

def main():

	# Example of input (it also works with strings)
	seq  = ['C', 'A', 'C', 'G', 'C', 'C', 'G', 'G', 'T', 'A', 'T', 'G', 'G', 'C', 'T', 'C', 'T', 'A', 'T', 'T', 'A', 'A', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'A', 'C', 'G', 'G', 'C', 'A', 'C']
	seq1 = ['C', 'A', 'C', 'G', 'C', 'C', 'G', 'G', 'T', 'A', 'T', 'G', 'G', 'C', 'T', 'C', 'T', 'A', 'T', 'T', 'A', 'A', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'A', 'C', 'G', 'G', 'C', 'A', 'C']
	seq2 = ['G', 'C', 'A', 'C', 'T', 'T', 'A', 'G', 'T', 'C', 'T', 'C', 'G', 'C', 'A', 'C', 'A', 'T', 'C', 'C', 'A', 'C', 'T', 'T', 'G', 'A', 'G', 'T', 'C', 'A', 'T', 'T', 'C', 'C', 'A', 'G']

	# Starting the class
	tools = ToolsToWorkWithSeq()

	# Calling the nucleotide_statistic function and printting the output
	stat = tools.nucleotide_statistics(seq)
	print(f'Nucleotide statistics for sequence: {stat}')

	print() # Formatting

	# Calling the observed_parwise_nucleotide_distance function and printting the result
	parwise = tools.observed_pairwise_nucleotide_distance(seq1, seq2)
	print(f'Nº of different nucleotides:  {parwise}')

	print() # Formatting

if __name__ == "__main__":
	main()