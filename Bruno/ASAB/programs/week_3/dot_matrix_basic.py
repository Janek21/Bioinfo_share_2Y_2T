def dot_matrix(seq1, seq2):
    '''
    >>> dot_matrix("FASTCAT", "FASTCAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "TACTSAF")
    [[' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], ['o', ' ', ' ', ' ', ' ', ' ', ' ']]
    '''
    M =[]
    for i in range(len(seq2)):
        row = []
        for j in range(len(seq1)):
            #print(seq2[i], seq1[j])
            if seq2[i] == seq1[j]:
                row.append('o')
            else:
                row.append(' ')
        M.append(row)

    return M


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
