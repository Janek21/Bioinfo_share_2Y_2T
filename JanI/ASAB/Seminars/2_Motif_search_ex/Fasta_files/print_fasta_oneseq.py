#!/usr/bin/python3


def print_fasta_oneseq(filename):
    '''
    >>> print_fasta(('fast_cat', 'THEFASTCAT'))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(('', 'THEFASTCAT'))
    >unnamed
    THEFASTCAT
    >>> print_fasta(('', ''))
    '''
    filename=list(filename)
    if filename[0]=="":
        if filename[1]=="":
            return
        filename[0]="unnamed"
    header=">"+filename[0]
    read=header+"\n"+filename[1]
    print(read)


print(print_fasta_oneseq(('fast_cat', 'THEFASTCAT')))


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)