def naive_match(p, t):
    '''
    >>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> naive_match('FAST', 'FAST')
    [0]
    >>> naive_match('FASTA', 'FAST')
    []
    '''

    # c = []
    # for i in range(len(t)):
    #     if t[i:i+len(p)] == p:
    #         c.append(i)
    # return c

    return [i for i in range(len(t) - len(p) + 1) if t[i:i+len(p)] == p]

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)