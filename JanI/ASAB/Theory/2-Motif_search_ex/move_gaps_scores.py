#!/usr/bin/python3
from move_gaps import move_gaps
from score_seqs_gap import score_seqs_gap as scores

def move_gaps_scores(seq1, seq2, match, mismatch, gap):
    '''
    >>> move_gaps_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)
    THEFASTCAT
    --AFASTCAT 2
    A--FASTCAT 2
    AF--ASTCAT 0
    AFA--STCAT -2
    AFAS--TCAT -4
    AFAST--CAT -6
    AFASTC--AT -8
    AFASTCA--T -10
    AFASTCAT-- -12
    >>> move_gaps_scores('AFASTCAT', 'THEFASTCAT', 1, -1, -2)
    THEFASTCAT
    --AFASTCAT 2
    A--FASTCAT 2
    AF--ASTCAT 0
    AFA--STCAT -2
    AFAS--TCAT -4
    AFAST--CAT -6
    AFASTC--AT -8
    AFASTCA--T -10
    AFASTCAT-- -12
    '''
    mv=move_gaps(seq1, seq2)
    if len(seq1)>len(seq2):#seq is the largest
        seq=seq1
    else:
        seq=seq2
    #setup={mv[0]:""}
    for pos in range(len(mv)):
        current_seq=mv[pos]
        if pos>0:
            #setup[current_seq]=scores(seq, current_seq, match, mismatch, gap)
            print(f"{current_seq} {scores(seq, current_seq, match, mismatch, gap)}")#setup[surrent_seq]
        else:
            print(current_seq)



if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)