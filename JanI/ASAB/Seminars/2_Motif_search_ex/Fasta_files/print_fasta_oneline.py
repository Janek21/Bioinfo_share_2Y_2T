#!/usr/bin/python3

from read_fasta_oneline import read_fasta_oneline as read_fasta #for doctest

def print_fasta_oneline(seqid_seq_dict):
    fasta_list=[]
    for entry in seqid_seq_dict:
        header=">"+entry
        fasta_list.append([header, seqid_seq_dict[entry]])

    return(fasta_list)

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
    result=print_fasta_oneline(seqid_seq_dict)
    for entry in result:
        print(entry[0])#key
        print(entry[1])#value


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
        

