def score_seqs(seq1, seq2, match, mismatch):

	'''
	>>> score_seqs("THEFASTCAT", "THEFASTCAT", 1, -1)
	10
	>>> score_seqs("THEFASTCAT", "THELASTCAT", 1, -1)
	8
	>>> score_seqs("THEFASTCAT", "THELASTRAT", 1, -1)
	6
	>>> score_seqs("THEFASTCAT", "THE", 1, -1)
	0
	'''

	m = 0
	n = 0

	
	if len(seq1) != len(seq2):
		return 0
		
	elif len(seq1) == len(seq2):
		for letra in range(len(seq1)):
			if seq1[letra] == seq2[letra]:
				m += 1
			else:
				n += 1
		
	score = m*match + n*mismatch
	return score

	
	
if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)
