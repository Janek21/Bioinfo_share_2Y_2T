from read_fasta_any import read_fasta

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
    >>> print_fasta({'many_cats': 'CAT' * 100})
    >many_cats
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    '''

    result = []
    for key in seqid_seq_dict:
        result.append(f'>{key}')
        line = seqid_seq_dict[key]

        ret = ''
        for x in line:
            if len(ret) < 60:
                ret += x
            else:
                result.append(ret)
                ret = x
        result.append(ret)

    for res in result:
        print(res)
    
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)