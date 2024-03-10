def move_gaps(seq1, seq2):

    result = []
    
    if len(seq1) > len(seq2):
        used = seq1
        main = seq2
    elif len(seq1) < len(seq2):
        used = seq2
        main = seq1
    result.append(used)
    n = len(used) - len(main) 
    for i in range(len(main)+1):
        
        result.append(main[:i] + '-' * n + main[i:])

    return result

def score_seqs(seq1, seq2, match, mismatch, gap):
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

def  move_gaps_scores(seq1, seq2, match, mismatch, gap):

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

    sequence = move_gaps(seq1, seq2)
    print(sequence[0])
    
    for x in range(1, len(sequence)): 
        print(f'{sequence[x]} {score_seqs(sequence[x], sequence[0], match, mismatch, gap)}')
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)