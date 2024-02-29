#!/usr/bin/python3
from Bio import SeqIO

def read_fasta_oneseq_SeqIO(filename):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+filename
    read=SeqIO.read(filename, "fasta")
    return (read.id, str(read.seq))


def read_fasta_oneseq(filename):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+filename
    file=open(filename, "r")
    for line in file:
        line=line.strip("\n")
        if line.startswith(">"):
            header=line[1:]
        else:
            tp=(header, line)
    file.close()
    return tp

print(read_fasta_oneseq('thefastcat.fasta'))
      
if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)