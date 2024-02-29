#!/usr/bin/python3

from read_fasta_oneline import read_fasta_oneline as read_fasta #for doctest
from print_fasta_oneline import print_fasta_oneline
import textwrap


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
    result=print_fasta_oneline(seqid_seq_dict) #list [[header, sequence], [header, sequence]], where header is the dictionary key and sequence is the value
    for entry in result:
        print(entry[0])#key
        print(textwrap.fill(entry[1], 60))#value, line break every 60 char


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)