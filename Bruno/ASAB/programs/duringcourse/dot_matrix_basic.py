
def dot_matrix(seq1, seq2):

    '''
    >>> dot_matrix("FASTCAT", "FASTCAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "TACTSAF")
    [[' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], ['o', ' ', ' ', ' ', ' ', ' ', ' ']]
    '''
    matrix = []
    for _ in range(len(seq2)):
        row = []
        for _ in range(len(seq1)):
            row.append(' ')
        matrix.append(row)
    
    
    for i in range(len(seq2)):

        for j in range(len(seq1)):
            
            if seq2[i] == seq1[j]:
                matrix[i][j] = 'o'
                
    return matrix

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)