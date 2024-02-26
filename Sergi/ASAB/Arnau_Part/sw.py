from Bio.Align import substitution_matrices

def sw(seq_i, seq_j, gap):
    '''
    >>> sw('THEFASTCAT', 'THERAT', -4)
    (20.0, ('THEFAS', 'THERAT'))
    >>> sw('FAT', 'THEFASTCAT', -4)
    (11.0, ('FAT', 'FAS'))
    '''
    # Load BLOSUM62 substitution matrix
    subst_mat = substitution_matrices.load("BLOSUM62")

    # Initialize matrices
    score_mat = [[0] * (len(seq_j) + 1) for _ in range(len(seq_i) + 1)]
    traceback = [[0] * (len(seq_j) + 1) for _ in range(len(seq_i) + 1)]

    # Keep track of maximum score and positions
    max_score = 0
    max_i, max_j = 0, 0

    # Fill matrices
    for i in range(1, len(seq_i) + 1):
        for j in range(1, len(seq_j) + 1):
            subst = score_mat[i - 1][j - 1] + subst_mat[seq_i[i - 1], seq_j[j - 1]]
            inser = score_mat[i][j - 1] + gap
            delet = score_mat[i - 1][j] + gap
            score = max(0, subst, inser, delet) 

            score_mat[i][j] = score
            if score > max_score:
                max_score = score
                max_i, max_j = i, j

            if score == subst:
                traceback[i][j] = 0
            elif score == inser:
                traceback[i][j] = -1
            elif score == delet:
                traceback[i][j] = 1

    # Perform traceback starting from the position of the maximum score
    aligned_seq_i = []
    aligned_seq_j = []
    i, j = max_i, max_j
    while score_mat[i][j] != 0:
        if traceback[i][j] == 0:
            aligned_seq_i.append(seq_i[i - 1])
            aligned_seq_j.append(seq_j[j - 1])
            i -= 1
            j -= 1
        elif traceback[i][j] == -1:
            aligned_seq_i.append('-')
            aligned_seq_j.append(seq_j[j - 1])
            j -= 1
        elif traceback[i][j] == 1:
            aligned_seq_i.append(seq_i[i - 1])
            aligned_seq_j.append('-')
            i -= 1

    # Reverse alignments
    aligned_seq_i.reverse()
    aligned_seq_j.reverse()

    return max_score, (''.join(aligned_seq_i), ''.join(aligned_seq_j))


# Testing the function with provided test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
