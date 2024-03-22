def nw(seq_i, seq_j, match, mismatch, gep):
    """Returns the global sequence alignment of seq_i and seq_j
    by using the match, mismatch and gep parameters
    >>> nw('FAT', 'FAST', 2, -1, -1)
    ('FA-T', 'FAST')
    >>> nw('THEFASTCAT', 'THERAT', 1, -8, -4)
    ('THE-FASTCAT', 'THER-A-T---')
    >>> nw('THERAT', 'THEFASTCAT', 1, -8, -4)
    ('THE-RA-T---', 'THEF-ASTCAT')
    """
    
    ties=0
    # We initialize the matrices
    score_mat = [[0 for _ in range(len(seq_j) + 1)] for _ in range(len(seq_i) + 1)]
    traceback = [[0 for _ in range(len(seq_j) + 1)] for _ in range(len(seq_i) + 1)]

    for i in range(1, len(seq_i) + 1):
        score_mat[i][0] = i * gep
        traceback[i][0] = 1

    for j in range(1, len(seq_j) + 1):
        score_mat[0][j] = j * gep
        traceback[0][j] = -1

    # We fill the matrices
    for i in range(1, len(seq_i) + 1):
        for j in range(1, len(seq_j) + 1):
            score = match if seq_i[i - 1] == seq_j[j - 1] else mismatch
            subst = score_mat[i - 1][j - 1] + score
            inser = score_mat[i][j - 1] + gep
            delet = score_mat[i - 1][j] + gep
            
            mx=max(subst, inser, delet) ##NEW

            if subst > inser and subst > delet:
                score_mat[i][j] = subst
                traceback[i][j] = 0
            elif inser > delet:
                score_mat[i][j] = inser
                traceback[i][j] = -1
            else:
                score_mat[i][j] = delet
                traceback[i][j] = 1

            if [inser, subst, delet].count(mx)>1: ##NEW
                ties+=1                     ## Do a tie for every match, multiple matches count as 1

    # for row in traceback:
    #     print(row)
    # We do the traceback
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

    return ties ##NEW
    return "".join(reversed(aln_i)), "".join(reversed(aln_j))


print(nw("FAT", "FAST", 2, -1, -1))
