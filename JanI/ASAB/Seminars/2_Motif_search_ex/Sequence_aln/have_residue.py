#!/usr/bin/python3

from Bio import SeqIO

def have_residue(fasta_file, residue, mincount):
    '''
    >>> have_residue("fastcats.fasta", "E", 2)
    1
    >>> have_residue("fastcats.fasta", "T", 2)
    4
    >>> have_residue("fastcats.fasta", "W", 0)
    4
    >>> have_residue("fastcats.fasta", "W", 1)
    0
    >>> have_residue("fastcats.fasta", "", 1)
    0
    '''
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+fasta_file
    total=0
    if residue:
        for read in SeqIO.parse(filename, "fasta"):
            seq=read.seq
            nucl_in_seq=seq.count(residue)
            if nucl_in_seq>=mincount:
                total+=1
        return total
    return total


print(have_residue("fastcats.fasta", "E", 2))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)