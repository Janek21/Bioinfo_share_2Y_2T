def naive_match(p, t):
    '''
    >>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> naive_match('FAST', 'FAST')
    [0]
    >>> naive_match('FASTA', 'FAST')
    []
    '''
    offsets = []

    
    for i in range(len(t) - len(p) + 1):
        match = True

        
        for j in range(len(p)):
            if t[i + j] != p[j]:
                match = False
                break

        if match:
            offsets.append(i)

    return offsets


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
     

