def score_seqs(seq_1, seq_2, match, mismatch, gap):
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

	score = 0
	
	if len(seq_1) != len(seq_2):
		return 0
	
	else:

		for i in range(len(seq_1)):

			if seq_1[i] == '-' or seq_2[i] == '-':
				score += gap

			elif seq_1[i] == seq_2[i]:
				score += match

			else:
				score += mismatch

	return score