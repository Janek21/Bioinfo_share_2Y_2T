def needleman_wunsch(sequence_1, sequence_2, match_score, mismatch_penalty, gap_penalty):
    '''
    >>> needleman_wunsch('ATCGATGCTATGCTAAATACGAT', 'UCGAUGCUAUCUAAAUAACGAU', 1, -8, -4)
    ('ATCGATGCTATGCTAAA-TACGAT', '-UCGAUGCUA-UCUAAAUAACGAU')
    >>> needleman_wunsch('UCGAUGCUAUCUAAAUAACGAU', 'ATCGATGCTATGCTAAATACGAT', 1, -8, -4)
    ('-UCGAUGCUA-UCUAAAUAACGAU', 'ATCGATGCTATGCTAAA-TACGAT')
    '''
    #initializeing score and traceback matrices
    score_matrix = [[0 for _ in range(len(sequence_2) + 1)] for _ in range(len(sequence_1) + 1)]
    traceback_matrix = [[0 for _ in range(len(sequence_2) + 1)] for _ in range(len(sequence_1) + 1)]

    #initializing scores for gaps
    current_score = 0
    for i in range(len(sequence_1) + 1):
        score_matrix[i][0] = current_score
        traceback_matrix[i][0] = 1  #arrow is pointing up
        current_score += gap_penalty

    current_score = 0
    for j in range(len(sequence_2) + 1):
        score_matrix[0][j] = current_score
        traceback_matrix[0][j] = -1  #arrow is pointing left
        current_score += gap_penalty

    #filling in the score matrix
    for i in range(1, len(sequence_1) + 1):
        for j in range(1, len(sequence_2) + 1):
            if sequence_1[i - 1] == sequence_2[j - 1]:
                score = match_score
            else:
                score = mismatch_penalty

            #computing scores for substitution, insertion and deletion
            substitution = score_matrix[i - 1][j - 1] + score
            insertion = score_matrix[i][j - 1] + gap_penalty
            deletion = score_matrix[i - 1][j] + gap_penalty

            #choosing the max score and updating the traceback matrix
            if deletion > substitution and deletion > insertion:
                score_matrix[i][j] = deletion
                traceback_matrix[i][j] = 1  #arrow is pointing up
            elif insertion > substitution:
                score_matrix[i][j] = insertion
                traceback_matrix[i][j] = -1  #arrow is pointing left
            else:
                score_matrix[i][j] = substitution
                traceback_matrix[i][j] = 0  #arrow is pointing diagonal

    #traceback for finding the aligned sequences
    aligned_sequence_1 = []
    aligned_sequence_2 = []

    i = len(sequence_1)
    j = len(sequence_2)

    while i != 0 or j != 0:
        if traceback_matrix[i][j] == 0:  #moving diagonaly
            i -= 1
            j -= 1
            aligned_sequence_1.append(sequence_1[i])
            aligned_sequence_2.append(sequence_2[j])
        elif traceback_matrix[i][j] == -1:  #moving horizontaly ( there is a gap in sequence_1)
            j -= 1
            aligned_sequence_1.append("-")
            aligned_sequence_2.append(sequence_2[j])
        else:  #moving vertically (there is agap in sequence_2)
            i -= 1
            aligned_sequence_1.append(sequence_1[i])
            aligned_sequence_2.append("-")

    #reversing and joining the aligned sequences
    aligned_sequence_1 = ''.join(map(str, reversed(aligned_sequence_1)))
    aligned_sequence_2 = ''.join(map(str, reversed(aligned_sequence_2)))

    return aligned_sequence_1, aligned_sequence_2

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
#subst matrix
