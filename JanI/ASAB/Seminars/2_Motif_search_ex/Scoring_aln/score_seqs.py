#!/usr/bin/python3
import sys

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
    if abs(mismatch)>(len(seq1)) or len(seq1)!=len(seq2):
        return 0
    if seq1[mismatch]==seq2[mismatch]:
        return match+score_seqs(seq1, seq2, match, mismatch-1)
    return -1+score_seqs(seq1, seq2, match, mismatch-1)

print(score_seqs("THEFASTCAT", "THELASTCAT", 1, -1))


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
