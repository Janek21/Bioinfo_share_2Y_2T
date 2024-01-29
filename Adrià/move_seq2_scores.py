
def move_seq2(seq1, seq2):
    tot=[]
    guio='-'*(len(seq1)+len(seq2))
    tot.append(seq1+'-'*len(seq2))
    for x in range(len(seq1)+1):
        tot.append(guio[0:x] + seq2 + guio[x+len(seq2):])
    return(tot)

def score_seqs(seq1, seq2, mach, mismach,gap):

    if len(seq1)!=len(seq2):
        return 0
    tot=[]
    for x in range(len(seq1)):
        if seq1[x]=='-' or seq2[x]=='-':
            tot.append(gap)
        elif seq1[x]==seq2[x]:
            tot.append(mach)
        else:
            tot.append(mismach)
    return(sum(tot))




def move_seq2_scores(seq1, seq2, mach, mismach, gap):
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
    t=move_seq2(seq1,seq2)
    print(t[0])
    for x in t[1:]:
        p=score_seqs(t[0], x, mach, mismach,gap)
        
        print(f'{x} {p}')
