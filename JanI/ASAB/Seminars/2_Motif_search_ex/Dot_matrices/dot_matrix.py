#!/usr/bin/python3

def dot_matrix(seq1, seq2):
    '''
    >>> dot_matrix("FASTCAT", "FASTCAT")
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "TACTSAF")
    [[' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', 'o', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', 'o', ' ', ' '], [' ', ' ', ' ', 'o', ' ', ' ', 'o'], [' ', ' ', 'o', ' ', ' ', ' ', ' '], [' ', 'o', ' ', ' ', ' ', 'o', ' '], ['o', ' ', ' ', ' ', ' ', ' ', ' ']]
    '''
    M=[[" " for _ in range(len(seq1))] for _ in range(len(seq2))]
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i]==seq2[j]:
                M[j][i]="o"

    return M

a=dot_matrix("FASTCAT", "TACTSAF")

for x in a:
    print(*x)


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
