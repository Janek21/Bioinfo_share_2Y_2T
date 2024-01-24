def many_finds(p, t):
    '''
    >>> many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> many_finds('FAST', 'FAST')
    [0]
    >>> many_finds('FASTA', 'FAST')
    []
    '''

    i = 0
    output = []

    while i < len(t):
        
        find = t.find(p, i)

        if find != -1:

            output.append(find)

            i = find + len(p) - 1
        
        else:
            return output

if __name__ == "__main__":
	
	import doctest
	doctest.testmod(verbose=True)