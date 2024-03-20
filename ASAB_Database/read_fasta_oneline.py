#!/usr/bin/python3
from Bio import SeqIO

def read_fasta_oneline_SeqIO(filename):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+filename
    readlist={}
    for read in SeqIO.parse(filename, "fasta"):
        readlist[read.id]=str(read.seq)
    return readlist

def read_fasta_oneline(filename):
    '''
    >>> read_fasta_oneline('thefastcat.fasta')
    {'fast_cat': 'THEFASTCAT'}
    >>> read_fasta_oneline('fastcats.fasta')
    {'FAST_CAT': 'THE----FASTCAT', 'FAT_RAT': 'THE----FA-TRAT', 'VERYFAST_CAT': 'THEVERYFASTCAT', 'LAST_CAT': '---LASTFA-TCAT'}
    '''
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+filename
    readlist={}
    file=open(filename, "r")
    for line in file:
        line=line.strip("\n")
        if line.startswith(">"):
            readlist[line[1:]]="" #add to dict line except >
        else:
            last_key=list(readlist)[-1] #if line does not start with  >, take last line that has > as key
            readlist[last_key]+=line #using last_key as key, add current line as value
    file.close()
    return readlist
             
        
        

print(read_fasta_oneline('fastcats.fasta'))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)