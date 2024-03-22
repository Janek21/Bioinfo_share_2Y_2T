#!/usr/bin/python3

from Bio import SeqIO

def count_matches_stars(fasta_file):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+fasta_file
    ls=[]
    for read in SeqIO.parse(filename, "fasta"):
        ls.append(str(read.seq))

    ls.append("")
    for pos in range(len(ls[0])):

        for seq_pos in range(1, len(ls)-1):

            last_seq=ls[seq_pos-1]
            current_seq=ls[seq_pos]

            if current_seq[pos]==last_seq[pos]:
                t=0
            else:
                t=1
                ls[-1]+=" "
                break

        if t==0:
            ls[-1]+="*"
    return ls

def main():
    res=count_matches_stars("fastcats.fasta")
    for ls in res:
        print(ls)

print(main())

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)

    
