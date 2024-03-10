def print_fasta(tuple):
    '''
    >>> print_fasta(('fast_cat', 'THEFASTCAT'))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(('', 'THEFASTCAT'))
    >unnamed
    THEFASTCAT
    >>> print_fasta(('', ''))
    '''
    
    filename = str(tuple[0])
    
    if filename == '':
        filename = 'unnamed'
    
    seq = str(tuple[1])
    
    if seq == '':
       return

    print('>' + filename)
    print(seq)

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)