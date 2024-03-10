def dot_matrix(seq1, seq2, n = 1):
    '''
    >>> dot_matrix("FASTCAT", "FATRAT", 2)
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> dot_matrix("FASTCAT", "FATRAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "FATRAT", 0)
    Window should be 1 or larger
    '''
    if n < 1:
        print('Window should be 1 or larger')
        return
    
    M = []
    #print(n)
    for i in range(len(seq2)):
        row = []
        for j in range(len(seq1)):
            #print(seq1[j:j+n], seq2[i:i+n])
            if seq1[j:j+n] == seq2[i:i+n] and (len(seq1[j:j+n]) and len(seq2[i:i+n])) == n:
                row.append('o')
            else:
                row.append(' ')
        M.append(row)
    return M

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)