
from Bio import SeqIO

def count_matches_multiple(fasta_file):
    filename="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S2_Motif_search_ex/data/"+fasta_file
    ls=[]
    for read in SeqIO.parse(filename, "fasta"):
        ls.append(str(read.seq))
    c=0

    for pos in range(len(ls[0])):
        #print(ls)
        for seq_pos in range(1, len(ls)):
            last_seq=ls[seq_pos-1]
            current_seq=ls[seq_pos]

            if current_seq[pos]==last_seq[pos]:
                t=0
            else:
                t=1
                break

        if t==0:
            c+=1
    return c

print(count_matches_multiple("fastcats.fasta"))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
    