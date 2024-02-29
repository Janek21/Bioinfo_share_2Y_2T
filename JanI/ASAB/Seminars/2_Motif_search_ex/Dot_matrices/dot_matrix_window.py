#!/usr/bin/python3

#No pots tenir menys arguments, cas 2 com es fa?
    #si altre funcio, que fas quan en tens 3?

def dot_matrix_window(seq1, seq2, size=None):
    '''
    >>> dot_matrix_window("FASTCAT", "FATRAT", 2)
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> dot_matrix_window("FASTCAT", "FATRAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    >>> dot_matrix_window("FASTCAT", "FATRAT", 0)
    "Window should be 1 or larger"
    '''
    M=[[" " for _ in range(len(seq1))] for _ in range(len(seq2))]
    if size==0:
        return "Window should be 1 or larger"
    if not size:
        size=1
    for i in range(len(seq1)-size+1):

        for j in range(len(seq2)-size+1):

            if seq1[i:i+size]==seq2[j:j+size]:
                M[j][i]="o"

    return M

#print(dot_matrix_window("FASTCAT", "FATRAT", 2))
     
if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)

