def score_seqs_gap(seq1, seq2, match, mismatch, gap):
    '''  
    >>> score_seqs_gap("THEFASTCAT", "THEFATCAT-", 1, -1, -2)
    -1
    >>> score_seqs_gap("THEFASTCAT", "THEFATCA-T", 1, -1, -2)
    1
    >>> score_seqs_gap("THEFA-TCAT", "THEFASTCAT", 1, -1, -2)
    7
    >>> score_seqs_gap("THEFASTCAT", "THE", 1, -1, -2)
    0
    >>> score_seqs_gap("THE-FASTCAT", "THE-FASTCAT", 1, -1, -2)
    8
    '''

    score = 0
    if len(seq1) != len(seq2):
        return score
    
    for i in range(len(seq1)):
        if seq1[i] == '-' or seq2[i] == '-':
            score += gap
        elif seq1[i] == seq2[i]:
            score += match
        else:
            score += mismatch
    return score


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)