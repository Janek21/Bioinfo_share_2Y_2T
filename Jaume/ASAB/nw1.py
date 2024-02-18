def nw1(seq_i, seq_j, match_score, mismatch_score, gap_score):
	'''
	>>> nw1('FAT', 'FAST', 2, -1, -1)
	('FA-T', 'FAST')
	>>> nw1('THEFASTCAT', 'THERAT', 1, -8, -4)
	('THE-FASTCAT', 'THER-A-T---')
	>>> nw1('THERAT', 'THEFASTCAT', 1, -8, -4)
	('THE-RA-T---', 'THEF-ASTCAT')
	'''
	
	# Initialize matrices for storing alignment scores and traceback information
	score_matrix = [[0] * (len(seq_j) + 1) for _ in range(len(seq_i) + 1)]
	traceback = [[0] * (len(seq_j) + 1) for _ in range(len(seq_i) + 1)]
	
	# Fill the first row and column of the matrices with gap penalties
	for i in range(1, len(seq_i) + 1):
		
		score_matrix[i][0] = gap_score * i
		traceback[i][0] = 1  # pointing up

	for j in range(1, len(seq_j) + 1):
		
		score_matrix[0][j] = gap_score * j
		traceback[0][j] = -1  # pointing left

	# Fill matrices by computing scores for each cell based on match, mismatch, and gap penalties
	for i in range(1, len(seq_i) + 1):
		
		for j in range(1, len(seq_j) + 1):
			
			if seq_i[i - 1] == seq_j[j - 1]:
				
				score = match_score
				
			else:
				
				score = mismatch_score
			
			substitution = score_matrix[i - 1][j - 1] + score
			insertion = score_matrix[i][j - 1] + gap_score
			deletion = score_matrix[i - 1][j] + gap_score

			# Choose the maximum score among substitution, insertion, and deletion
			if substitution > insertion and substitution > deletion:
				
				score_matrix[i][j] = substitution
				traceback[i][j] = 0  # diagonal arrow
				
			elif insertion > deletion:
				
				score_matrix[i][j] = insertion
				traceback[i][j] = -1  # left arrow
				
			else:
				
				score_matrix[i][j] = deletion
				traceback[i][j] = 1  # up arrow
	
	'''
	Traceback to reconstruct the aligned sequences
	'''
	
	aligned_seq_i = []
	aligned_seq_j = []
	
	i = len(seq_i)
	j = len(seq_j)
	
	# Iteration through i and j as indicators until they reach 0
	while i != 0 or j != 0:
		
		if traceback[i][j] == 0:

			aligned_seq_i.append(seq_i[i - 1])
			aligned_seq_j.append(seq_j[j - 1])

			i -= 1
			j -= 1
			
		elif traceback[i][j] == -1:

			aligned_seq_i.append('-')
			aligned_seq_j.append(seq_j[j - 1])

			j -= 1
			
		else:
			aligned_seq_i.append(seq_i[i - 1])
			aligned_seq_j.append('-')

			i -= 1
	
	# Reverse the alignments to get the correct order
	aligned_seq_i.reverse()
	aligned_seq_j.reverse()

	# From list to string:
	out_i = ''
	out_j = ''
	
	for i in aligned_seq_i: out_i += i
	for i in aligned_seq_j: out_j += i
	
	return out_i, out_j

if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)
