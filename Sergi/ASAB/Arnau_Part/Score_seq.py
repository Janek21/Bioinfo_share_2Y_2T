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
    # Check if the sequences have the same length
    if len(seq1) != len(seq2):
        return 0
    
    score = 0
   
    for i in range(len(seq1)):
        char1 = seq1[i]
        char2 = seq2[i]
        
        if char1 == char2:
            score += match
        else:
            score += mismatch
    
    return score




if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)