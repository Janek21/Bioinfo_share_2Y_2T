#!/usr/bin/python3
from move_seq2 import move_seq2
from score_seqs_gap import score_seqs_gap as scores

def move_seq2_scores(seq1, seq2, match, mismatch, gap):
    '''
    >>> move_seq2_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)
    THEFASTCAT--------
    AFASTCAT---------- -28
    -AFASTCAT--------- -28
    --AFASTCAT-------- -14
    ---AFASTCAT------- -29
    ----AFASTCAT------ -28
    -----AFASTCAT----- -29
    ------AFASTCAT---- -30
    -------AFASTCAT--- -33
    --------AFASTCAT-- -32
    ---------AFASTCAT- -35
    ----------AFASTCAT -36
    '''
    mv=move_seq2(seq1, seq2)
    seq=mv[0]
    #results={}
    results=[]
    for pos in range(len(mv)):
        current_seq=mv[pos]
        if pos>0:
            #results[current_seq]=scores(seq, current_seq, match, mismatch, gap)  
            results.append(f"{current_seq} {scores(seq, current_seq, match, mismatch, gap)}") 
        else:
            #print(current_seq)
            results.append(current_seq)
        #print(results)
    return results

print(move_seq2_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)