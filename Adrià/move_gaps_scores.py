def score_seqs(seq1, seq2, mach, mismach,gap):
    if len(seq1)!=len(seq2):
        return 0
    tot=[]
    for x in range(len(seq1)):
        if seq1=='-' or seq2=='-':
            tot.append(gap)
        elif seq1[x]==seq2[x]:
            tot.append(mach)
        else:
            tot.append(mismach)
    return(sum(tot))


def move_gaps(seq1, seq2):
    gaps=len(seq1)-len(seq2)
    long_seq=''
    short_seq=''
    tot=[]

    if gaps>0:
        tot.append(seq1)
        long_seq = seq1
        short_seq = seq2

    else:
        tot.append(seq2)
        long_seq = seq2
        short_seq = seq1
        gaps=gaps*-1
    for i in range(len(long_seq) - gaps + 1):
        tot.append(short_seq[:i] + '-' * gaps + short_seq[i:])

    return(tot)


def move_gaps_scores(seq1, seq2, mach, mismach, gap):
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
    p=move_gaps(seq1, seq2)
    g=p[0]
    print(g)
    for x in p[1:]: 
        t = score_seqs(g,x,mach,mismach,gap)-2    
        print(f'{x} {t}')
