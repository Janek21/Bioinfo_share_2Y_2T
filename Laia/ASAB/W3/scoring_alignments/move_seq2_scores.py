from move_seq2 import move_seq2
from score_seqs_gaps import score_seqs_gap

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

    sequencies = move_seq2(seq1, seq2)
    g = sequencies[0]
    
    res = [sequencies.pop(0)]
    for x in sequencies:
        score = score_seqs_gap(g, x, match, mismatch, gap)
        res.append(f'{x} {score}')

    print('\n'.join(res))

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)