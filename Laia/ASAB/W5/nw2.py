def nw(seq_i, seq_j, match, mismatch, gep):
    '''
    >>> nw('THEFASTCAT', 'THERAT', 1, -8, -4)
    ('THEF-ASTCAT', 'THE-RA-T---')
    >>> nw('THERAT', 'THEFASTCAT', 1, -8, -4)
    ('THER-A-T---', 'THE-FASTCAT')
  
    '''
    score_mat = [[0 for _ in range(len(seq_j)+1)] for _ in range(len(seq_i)+1)]
    traceback = [[0 for _ in range(len(seq_j)+1)] for _ in range(len(seq_i)+1)]

    c = 0
    for i in range(len(seq_i)+1):
        score_mat[i][0] = c
        traceback[i][0] = 1  # arrow pointing up
        c += gep

    c = 0
    for j in range(len(seq_j)+1):
        score_mat[0][j] = c
        traceback[0][j] = -1  # arrow pointing left
        c += gep

    for i in range(1, len(seq_i) + 1):
        for j in range(1, len(seq_j) + 1):
            if seq_i[i - 1] == seq_j[j - 1]:
                score = match
            else:
                score = mismatch
            
            subst = score_mat[i - 1][j - 1] + score
            inser = score_mat[i][j - 1] + gep
            delet = score_mat[i - 1][j] + gep

            if subst > inser and subst > delet:
                score_mat[i][j] = subst
                traceback[i][j] = 0
            elif delet > inser:
                score_mat[i][j] = delet
                traceback[i][j] = 1
            else:
                score_mat[i][j] = inser
                traceback[i][j] = -1

    aln_i = []
    aln_j = []

    i = len(seq_i)
    j = len(seq_j)

    while i != 0 or j != 0:
        if traceback[i][j] == 0:
            i -= 1
            j -= 1
            aln_i.append(seq_i[i])
            aln_j.append(seq_j[j])
        elif traceback[i][j] == -1:
            j -= 1
            aln_i.append("-")
            aln_j.append(seq_j[j])
        else:
            i -= 1
            aln_i.append(seq_i[i])
            aln_j.append("-")


    aln_i = ''.join(map(str, reversed(aln_i)))
    aln_j= ''.join(map(str, reversed(aln_j)))

    return aln_i, aln_j


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)