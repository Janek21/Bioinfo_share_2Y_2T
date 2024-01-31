#!/usr/bin/python3
import sys
from Bio.Align import substitution_matrices

def score_seqs_substmat(seq1, seq2, match, name):
    '''
    >>> score_seqs_substmat("THEFASTCAT", 
                            "THEFATCAT ", 1, "BLOSUM62")
    29
    >>> score_seqs_substmat("THEFASTCAT", 
                            "THEFATCA T", 1, "BLOSUM62")
    34
    >>> score_seqs_substmat("THEFA TCAT", 
                            "THEFASTCAT", 1, "BLOSUM62")
    52
    >>> score_seqs_substmat("THEFASTCAT", "THE", 1, "BLOSSUM62")
    0
    '''
    if match>(len(seq1)) or len(seq1)!=len(seq2):
        return 0
    subst_mat = substitution_matrices.load(name)
    amino1=seq1[match-1]
    amino2=seq2[match-1]
    if amino1==" ": amino1="*"
    if amino2==" ":amino2="*"
    print(f'for {amino1} and {amino2} number is {subst_mat[amino1][amino2]}')
    if amino1==amino2:
        return 1.0+subst_mat[amino1][amino2]+score_seqs_substmat(seq1, seq2, match+1, name)
    return subst_mat[amino1][amino2]+score_seqs_substmat(seq1, seq2, match+1, name)

subst_mat = substitution_matrices.load("BLOSUM62")
print(subst_mat)
print(score_seqs_substmat("THEFASTCAT", "THEFATCAT ", 1, "BLOSUM62"))
print(score_seqs_substmat("THEFASTCAT", "THEFATCA T", 1, "BLOSUM62"))
print(score_seqs_substmat("THEFA TCAT", "THEFASTCAT", 1, "BLOSUM62"))
'''
if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
'''