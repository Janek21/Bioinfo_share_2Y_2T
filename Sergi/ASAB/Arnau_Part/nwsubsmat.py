from Bio.Align import substitution_matrices

def nw(seq_i, seq_j, gap):
    '''
    >>> nw('FAT', 'FAST', -1)
    (14.0, 'FA-T', 'FAST')
    >>> nw('THEFASTCAT', 'THERAT', -4)
    (10.0, 'THEFASTCAT', 'THE---R-AT')
    >>> nw('THERAT', 'THEFASTCAT', -4)
    (10.0, 'THE---R-AT', 'THEFASTCAT')
    '''
   
    subst_mat = substitution_matrices.load("BLOSUM62")
    
   
    score_mat = [[0] * (len(seq_j) +   1) for _ in range(len(seq_i) +   1)]
    traceback = [[0] * (len(seq_j) +   1) for _ in range(len(seq_i) +   1)]
    
    for i in range(1, len(seq_i) +   1):
        score_mat[i][0] = gap * i
        traceback[i][0] =   1  #Going up

    for j in range(1, len(seq_j) +   1):
        score_mat[0][j] = gap * j
        traceback[0][j] = -1  #Going left

    
    for i in range(1, len(seq_i) +   1):
        for j in range(1, len(seq_j) +   1):
            # Use BLOSUM62 matrix for substitution score
            score = subst_mat[seq_i[i -   1], seq_j[j -   1]]
            
            subst = score_mat[i -   1][j -   1] + score
            inser = score_mat[i][j -   1] + gap
            delet = score_mat[i -   1][j] + gap

            if subst >= inser and subst >= delet:
                score_mat[i][j] = subst
                traceback[i][j] =   0
            elif inser >= delet:
                score_mat[i][j] = inser
                traceback[i][j] = -1
            else:
                score_mat[i][j] = delet
                traceback[i][j] =   1
    
    # Traceback
    aln_i = []
    aln_j = []
    i, j = len(seq_i), len(seq_j)
    while i !=   0 or j !=   0:
        if traceback[i][j] ==   0:
            aln_i.append(seq_i[i -   1])
            aln_j.append(seq_j[j -   1])
            i -=   1
            j -=   1
        elif traceback[i][j] == -1:
            aln_i.append('-')
            aln_j.append(seq_j[j -   1])
            j -=   1
        else:
            aln_i.append(seq_i[i -   1])
            aln_j.append('-')
            i -=   1
    
    # Reverse alignments   
    aln_i.reverse()
    aln_j.reverse()
    
    # Calculate and return the optimal score along with the aligned sequences
    optimal_score = score_mat[len(seq_i)][len(seq_j)]
    return optimal_score, ''.join(aln_i), ''.join(aln_j)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
