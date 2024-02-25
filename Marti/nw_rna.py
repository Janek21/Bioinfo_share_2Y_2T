def nw(seq1, seq2, match, mismatch, gap):
	'''
    >>> nw('ATCGATGCTATGCTAAATACGAT', 'UCGAUGCUAUCUAAAUAACGAU', 1, -8, -4)
    ('ATCGATGCTATGCTAAA-TACGAT', '-UCGAUGCUA-UCUAAAUAACGAU')
    >>> nw('UCGAUGCUAUCUAAAUAACGAU', 'ATCGATGCTATGCTAAATACGAT', 1, -8, -4)
    ('-UCGAUGCUA-UCUAAAUAACGAU', 'ATCGATGCTATGCTAAA-TACGAT')
	'''
	
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
			if seq1[i - 1] == seq2[j - 1]:
				match_score = match
			else:
				match_score = mismatch

			scores_alignment = scores[i - 1][j - 1] + match_score
			scores_insertion = scores[i][j - 1] + gap
			scores_deletion = scores[i - 1][j] + gap


			if scores_alignment >= scores_insertion and scores_alignment >= scores_deletion:
				scores[i][j] = scores_alignment
				traceback[i][j] = alignment

			elif scores_insertion >= scores_deletion:
				scores[i][j] = scores_insertion
				traceback[i][j] = insertion
				
			else:
				scores[i][j] = scores_deletion
				traceback[i][j] = deletion


	aligned1 = ""
	aligned2 = ""

	i = rows - 1
	j = cols - 1

		
	if 'U' in seq1:
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
	
	else:
		while i > 0 or j > 0:

			if traceback[i][j] == alignment:
				aligned1 += seq1[i - 1]
				aligned2 += seq2[j - 1]
				i -= 1
				j -= 1

			elif traceback[i][j] == insertion:
				aligned1 += '-'
				aligned2 += seq2[j - 1]
				j -= 1

			else:
				aligned1 += seq1[i - 1]
				aligned2 += '-'
				i -= 1

	result1 = aligned1[::-1]
	result2 = aligned2[::-1]

	return result1, result2


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
