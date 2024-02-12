def score_seqs(seq1, seq2, match, mismatch, gap):

	'''
	>>> score_seqs("THEFASTCAT", "THEFATCAT-", 1, -1, -2)
	-1
	>>> score_seqs("THEFASTCAT", "THEFATCA-T", 1, -1, -2)
	1
    >>> score_seqs("THEFA-TCAT", "THEFASTCAT", 1, -1, -2)
    7
    >>> score_seqs("THEFASTCAT", "THE", 1, -1, -2)
    0
    >>> score_seqs("THE-FASTCAT", "THE-FASTCAT", 1, -1, -2)
    8
	'''

	m = 0
	n = 0
	g = 0

	
	if len(seq1) != len(seq2):
		return 0
		
	elif len(seq1) == len(seq2):
		
		for letra in range(len(seq1)):
			if seq1[letra] == '-' or seq2[letra] == '-':
				g += 1
			
			elif seq1[letra] == seq2[letra]:
				m += 1 
			
			else:
				n += 1
		
	score = (m*match) + (n*mismatch) + (g*gap)
	return score
		
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
