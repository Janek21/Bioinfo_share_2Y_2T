#!/usr/bin/python3
import sys


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
    11
    '''
    if abs(mismatch)>(len(seq1)) or len(seq1)!=len(seq2):
        return 0
    if seq1[mismatch]==seq2[mismatch]:
        return match+score_seqs_gap(seq1, seq2, match, mismatch-1, gap)
    if seq1[mismatch]=="-" or seq2[mismatch]=="-":
        return gap+score_seqs_gap(seq1, seq2, match, mismatch-1, gap)
    return -1+score_seqs_gap(seq1, seq2, match, mismatch-1, gap)


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)