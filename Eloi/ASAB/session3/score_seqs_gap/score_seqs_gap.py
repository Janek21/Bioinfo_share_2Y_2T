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
	11
	'''
	s = 0
	cond = False
	if len(seq1) != len(seq2):
		return 0	
	for pos in range(len(seq1)):
		if seq1[pos] == seq2[pos]:
			s = s + match
		elif '-' in (seq1[pos], seq2[pos]):
			s+= gap
			cond = True
		else: s =  s+ mismatch
	return s

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose = True)
