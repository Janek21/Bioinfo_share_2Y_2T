def read_fasta(filename):
    '''
    >>> read_fasta('thefastcat.fasta')
    ('fast_cat', 'THEFASTCAT')
    '''

    directory = '/home/laia/Desktop/ASAB/Week3/aa_material/'+ filename
    with open(directory, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip()[1:]
        seq = lines[1].strip()
        return (header, seq)

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
