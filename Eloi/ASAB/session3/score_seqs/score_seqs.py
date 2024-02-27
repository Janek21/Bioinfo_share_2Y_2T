
def score_seqs(seq1, seq2, score_update, pos):
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
	if len(seq1) != len(seq2):
		return 0		
	if -pos > len(max([seq1,seq2])):
		return 0
		
	if seq1[pos] == seq2[pos]:
		return score_update + score_seqs(seq1, seq2, score_update, pos-1)
		
	return -score_update + score_seqs(seq1, seq2, score_update, pos-1)


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose = True)
