#!/usr/bin/python3

#IF NOT ENOGH ARGUMENTS TF I GOTTA DO
def dot_matrix_treshold(seq1, seq2, size=1, treshold=999):
    '''
    >>> dot_matrix_treshold("FASTCAT", "FATRAT", 2, 4)
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    >>> dot_matrix_treshold("FASTCAT", "FATRAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    '''
    if treshold<=size:
        return "A threshold smaller or equal than the window does not make sense"
    M=[[" " for _ in range(len(seq1))] for _ in range(len(seq2))]

    if size==0:
        return "Window should be 1 or larger"
    total=0
    for i in range(0, len(seq1)):
        for j in range(0, len(seq2)):
            #print(seq1[i:i+size], "and", seq2[j:j+size])
            if seq1[i:i+size]==seq2[j:j+size] and total<treshold:
                if len(seq1[i:i+size])>1:
                    M[j][i]="o"

    return M

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)