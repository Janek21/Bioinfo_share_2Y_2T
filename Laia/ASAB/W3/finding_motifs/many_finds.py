def many_finds(p, t):
    '''
    >>> many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> many_finds('FAST', 'FAST')
    [0]
    >>> many_finds('FASTA', 'FAST')
    []
    '''

    c = []
    # sequencia.find(paraula, start, end)
    seq = t.find(p)
    while seq != -1:
        c.append(seq)
        seq = t.find(p, seq+1)
    return c

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)


