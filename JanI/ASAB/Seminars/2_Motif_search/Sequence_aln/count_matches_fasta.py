
from Bio import SeqIO

def count_matches_fasta(fasta_file):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+fasta_file
    ls=[]
    for read in SeqIO.parse(filename, "fasta"):
        ls.append(str(read.seq))
    c=0
    seq1=ls[0]
    seq2=ls[1]
    for pos in range(len(seq1)):
        if seq1[pos]==seq2[pos]:
            c+=1
    return c

print(count_matches_fasta("cat_and_rat.fasta"))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)

    