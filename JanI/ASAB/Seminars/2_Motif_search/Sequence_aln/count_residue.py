#!/usr/bin/python3

from Bio import SeqIO

def count_residue(fasta_file, residue):
    '''
    >>> count_residue("fastcats.fasta", "T")
    12
    >>> count_residue("fastcats.fasta", "A")
    9
    >>> count_residue("fastcats.fasta", "U")
    0
    >>> count_residue("fastcats.fasta", "")
    0
    '''
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+fasta_file
    total=0
    if residue:
        for read in SeqIO.parse(filename, "fasta"):
            seq=read.seq
            total+=seq.count(residue)
        return total
    return total

#print(count_residue("fastcats.fasta", "T"))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)