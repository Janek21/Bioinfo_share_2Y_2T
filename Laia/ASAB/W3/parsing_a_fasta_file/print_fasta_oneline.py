from read_fasta_oneline import read_fasta

def print_fasta(seqid_seq_dict):
    '''
    >>> print_fasta({'fast_cat': 'THEFASTCAT'})
    >fast_cat
    THEFASTCAT
    >>> print_fasta(read_fasta("thefastcat.fasta"))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(read_fasta("fastcats.fasta"))
    >FAST_CAT
    THE----FASTCAT
    >FAT_RAT
    THE----FA-TRAT
    >VERYFAST_CAT
    THEVERYFASTCAT
    >LAST_CAT
    ---LASTFA-TCAT
    '''

    for key in seqid_seq_dict:
        print('>', key, sep = '')
        print(seqid_seq_dict[key])
    
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
