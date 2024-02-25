from Bio.Align import substitution_matrices

def nw(seq1, seq2, gap):
	'''
    >>> nw('FAT', 'FAST', -1)
    (14.0, 'FA-T', 'FAST')
    >>> nw('THEFASTCAT', 'THERAT', -4)
    (10.0, 'THEFASTCAT', 'THE---R-AT')
    >>> nw('THERAT', 'THEFASTCAT', -4)
    (10.0, 'THE---R-AT', 'THEFASTCAT')
	'''
	
	
	subst_mat = substitution_matrices.load("BLOSUM62")
	
	rows = len(seq1) + 1
	cols = len(seq2) + 1
	
	deletion = 'up'
	insertion = 'left'
	alignment = 'diagonal'
	
	scores = [[0] * cols for _ in range(rows)]
	traceback = [[0] * cols for _ in range(rows)]

	for i in range(1, rows):
		scores[i][0] = gap * i

	for j in range(1, cols):
		scores[0][j] = gap * j

	for i in range(1, rows):
		for j in range(1, cols):
			
			scores_alignment = scores[i - 1][j - 1] + subst_mat[seq1[i - 1]][seq2[j - 1]]
			scores_deletion = scores[i - 1][j] + gap
			scores_insertion = scores[i][j - 1] + gap
			
			scores[i][j] = max(scores_alignment, scores_deletion, scores_insertion)

			if scores[i][j] == scores_alignment:
				traceback[i][j] = alignment
			elif scores[i][j] == scores_deletion:
				traceback[i][j] = deletion
			else:
				traceback[i][j] = insertion

	score = scores[-1][-1]
	
	aligned1 = ''
	aligned2 = ''

	i = rows - 1
	j = cols - 1

	while i > 0 or j > 0:
		if traceback[i][j] == alignment:
			aligned1 += seq1[i - 1]
			aligned2 += seq2[j - 1]
			i -= 1
			j -= 1
			
		elif traceback[i][j] == deletion:
			aligned1 += seq1[i - 1]
			aligned2 += '-'
			i -= 1
		
		else:
			aligned1 += '-'
			aligned2 += seq2[j - 1]
			j -= 1
	
	result1 = aligned1[::-1]
	result2 = aligned2[::-1]

	return score, result1, result2
    
if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)
