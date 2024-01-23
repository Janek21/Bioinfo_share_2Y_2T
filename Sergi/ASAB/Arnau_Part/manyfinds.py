def many_finds(p, t):
    '''
    >>> many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> many_finds('FAST', 'FAST')
    [0]
    >>> many_finds('FASTA', 'FAST')
    []
    '''
    offsets = []
    index = t.find(p)

    while index != -1:
        offsets.append(index)
        index = t.find(p, index + 1)

    return offsets




if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
     
