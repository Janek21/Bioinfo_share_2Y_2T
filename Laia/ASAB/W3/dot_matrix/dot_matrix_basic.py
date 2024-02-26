def many_finds(p, t):
    c = []
    seq = t.find(p)
    while seq != -1:
        c.append(seq)
        seq = t.find(p, seq+1)
    return c

def dot_matrix(seq1, seq2):
    '''
    >>> dot_matrix("FASTCAT", "FASTCAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "TACTSAF")
    [[' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], ['o', ' ', ' ', ' ', ' ', ' ', ' ']]
    '''

    # create an empty matrix
    M = [[' ' for _ in range(len(seq1))] for _ in range(len(seq2))]

    # add the o when it finds the match
    for i in range(len(seq2)):
        for x in many_finds(seq2[i], seq1):
            M[i][x] = 'o'
    
    return M

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)