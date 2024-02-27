
def score_seqs(seq1, seq2, score_up, score_down):
	return sum([score_up if seq1[pos] == seq2[pos] else score_down for pos in range(len(max([seq1,seq2])))])


print(score_seqs("THEFASTCAT", "THELASTCAT", 1, -1))
