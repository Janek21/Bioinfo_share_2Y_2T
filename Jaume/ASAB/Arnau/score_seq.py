def score_seqs(seq_1, seq_2, good, wrong):
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
	
	score = 0
	
	if len(seq_1) != len(seq_2):
		return 0
	
	else:

		for i in range(len(seq_1)):

			if seq_1[i] == seq_2[i]:
				score += good

			else:
				score += wrong

	return score

def score_seqs_recursive(seq_1, seq_2, pos, score):
	'''
	>>> score_seqs("THEFASTCAT", "THEFASTCAT", 0, 0)
	10
	>>> score_seqs("THEFASTCAT", "THELASTCAT", 0, 0)
	8
	>>> score_seqs("THEFASTCAT", "THELASTRAT", 0, 0)
	6
	>>> score_seqs("THEFASTCAT", "THE", 0, 0)
	0  
	'''

	if len(seq_1) == len(seq_2):
		return 0
	
	if seq_2[pos] == seq_2[pos]:
		return score_seqs_recursive(seq_1, seq_2, pos + 1, score + 1)
	
	else:
		return score_seqs_recursive(seq_1, seq_2, pos + 1, score - 1)

	return 0