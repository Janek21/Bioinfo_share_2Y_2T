def many_finds(p, t):
    '''
    >>> many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> many_finds('FAST', 'FAST')
    [0]
    >>> many_finds('FASTA', 'FAST')
    []
    '''
    lista = []
    a = True
    while a == True:
        i = t.find(p)

        if i == -1:
            a = False
        
        else:
            lista.append(i)
            t = t[:i] + '-' * len(p) + t[i + len(p):]
    
    return lista

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)

