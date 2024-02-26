def dot_matrix_full(seq1, seq2, window, threshold):
    '''
    >>> dot_matrix("FASTCAT", "FATRAT", 4, 2)
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', 'o', ' ', ' ', ' ', ' '], [' ', ' ', 'o', 'o', ' ', ' ', ' '], [' ', ' ', ' ', 'o', 'o', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "FATRAT", 2, 4)
    A threshold larger or equal than the window does not make sense
    '''

    if window < 1:
        return "Window should be 1 or larger"
    elif threshold >= window:
        return "A threshold larger or equal than the window does not make sense"
    else:
        matriz = [[' ' for ]]

    #######
