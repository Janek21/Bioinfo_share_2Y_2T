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
    if len(seq1) != len(seq2):
          return 0
    z = 0
    for x in range(len(seq1)):
        if seq1[x] != seq2[x] or seq1[x] == '-' or seq2[x] == '-':
            if seq1[x] == '-' or seq2[x] == '-':
                z += gap
            else:
                z += mismatch
        else:
             z += match
    return z

    
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)