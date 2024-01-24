
    
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
    if len(seq1) != len(seq2):
        return 0
    z = 0
    for x in range(len(seq1)):
        if seq1[x] == seq2[x]:
              z += match
        else:
             z += mismatch
    return z

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)    
    

