def nw(seq1, seq2, match, mismatch, gep):
    '''
    >>> nw('FAT', 'FAST', 2, -1, -1)
    ('FA-T', 'FAST')
    >>> nw('THEFASTCAT', 'THERAT', 1, -8, -4)
    ('THE-FASTCAT', 'THER-A-T---')
    >>> nw('THERAT', 'THEFASTCAT', 1, -8, -4)
    ('THE-RA-T---', 'THEF-ASTCAT')
    '''

    # Initialize the matrix score
    score_mat = [[0 for x in range(len(seq2)+1)] for y in range(len(seq1)+1)]

    score_match_or_not = ''
    for i  in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
                if  seq1[i-1] == seq2[j-1]:
                        score_match_or_not = match
                else:
                        score_match_or_not = mismatch
                score_mat[i][j] = max(score_mat[i-1][j] + gep, score_mat[i][j-1] + gep, score_mat[i-1][j-1] + score_match_or_not)


if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)

