def print_fasta(filename):
    '''
    >>> print_fasta(('fast_cat', 'THEFASTCAT'))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(('', 'THEFASTCAT'))
    >unnamed
    THEFASTCAT
    >>> print_fasta(('', ''))
	'''

    header = filename[0]
    seq = filename[1]
    if seq != '':
        if header == '':
            print('>unnamed')
        else:
            print(f'>{header}')
        print(seq)


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)