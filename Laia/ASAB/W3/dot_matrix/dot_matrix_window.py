def dot_matrix(seq1, seq2, win):
    '''
    >>> dot_matrix("FASTCAT", "FATRAT", 2)
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> dot_matrix("FASTCAT", "FATRAT", 0)
    Window should be 1 or larger
    '''

    M = [[' ' for _ in range(len(seq1))] for _ in range(len(seq2))]
    
    if win == 0:
        print('Window should be 1 or larger')

    else:
        for i in range(len(seq1)-win+1):
            for j in range(len(seq2)-win+1):
                if seq1[i:i+win] == seq2[j:j+win]:
                    M[j][i] = 'o'
        return M

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)