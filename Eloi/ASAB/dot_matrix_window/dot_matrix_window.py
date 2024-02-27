def dot_matrix(seq1,seq2, w=1):
	'''
	>>> dot_matrix("FASTCAT", "FATRAT", 2)
	[['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
	>>> dot_matrix("FASTCAT", "FATRAT")
	[['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
	>>> dot_matrix("FASTCAT", "FATRAT", 0)
	Window should be 1 or larger
	''' 
	# Check if the window size is valid
	if w == 0:
		print('Window should be 1 or larger')
		return
		
	# Initialize an empty list to store the dot matrix
	l = []
	
	# Sort the input sequences based on length
	so = sorted([seq1, seq2], key=len)
	
	# Iterate through positions in the shorter sequence
	for x in range(len(so[0])):
		# Create a dot plot for the current position using a list comprehension
		dot_plot = ['o' if so[0][x:x+w] == so[1][pos:pos+w] and len(so[1]) - pos + 1 > w else ' ' for pos in range(len(so[1]))]
				# [do this if...								and if....				   if not do this] for every position in sequence  					
		l.append(dot_plot)

	return l

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose = True)
