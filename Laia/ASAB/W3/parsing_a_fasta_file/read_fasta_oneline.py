def read_fasta(filename):
    '''
    >>> read_fasta('thefastcat.fasta')
    {'fast_cat': 'THEFASTCAT'}
    >>> read_fasta('fastcats.fasta')
    {'FAST_CAT': 'THE----FASTCAT', 'FAT_RAT': 'THE----FA-TRAT', 'VERYFAST_CAT': 'THEVERYFASTCAT', 'LAST_CAT': '---LASTFA-TCAT'}
    '''

    directory = '/home/laia/Desktop/ASAB/Week3/aa_material/'+ filename
    header2seq = {}
    with open(directory, 'r') as f:
        line = f.readlines()
        n = len(line)

        c = 0
        while c != n:
            header = line[c].strip()[1:]
            seq = line[c+1].strip()
            header2seq[header] = seq
            c += 2
        return header2seq

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
