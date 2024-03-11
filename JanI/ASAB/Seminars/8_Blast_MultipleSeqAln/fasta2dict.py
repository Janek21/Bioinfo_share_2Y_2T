#!/usr/bin/python3
#credit to other github users

from Bio import SeqIO

def fasta2dict(filename):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S8_Blast_MultipleSeqAln/data/"+filename
    readlist={}

    for read in SeqIO.parse(filename, "fasta"):
        readlist[read.id]=read.seq
    
    return readlist

#print(fasta2dict('cats.fasta'))
'''
>>> fasta2dict('cats.fasta')
{'FAST_CAT': Seq('thefastcat'), 'FAT_CAT': Seq('a--fa-tcat')}
>>> fasta2dict('rats.fasta')
{'A_RAT': Seq('a--rat-'), 'THE_RATS': Seq('therats')}
'''
if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)