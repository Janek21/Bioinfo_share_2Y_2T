def naive_match(p, t):
    ''''
    >>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> naive_match('FAST', 'FAST')
    [0]
    >>> naive_match('FASTA', 'FAST')
    []
    '''
    lista = []
    for i in range(len(t)):
        if p == t[i:i + len(p)]:
            lista.append(i)
    return lista

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)