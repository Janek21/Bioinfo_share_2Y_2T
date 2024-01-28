#!/usr/bin/python3

from Bio import SeqIO
from read_fasta_oneline import read_fasta_oneline as read_fasta

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
    res=print_fasta_oneline(seqid_seq_dict)
    for x in res:
        print(x[0])
        print(x[1])


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
        

