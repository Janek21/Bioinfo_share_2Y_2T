#!/usr/bin/python3
from needleman3 import nw3, tracer
##depen de que es ultim paraeter

from Bio import SeqIO

def sequencereader(file, n1, n2, match):
    file="/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Seminars/S4_/data/"+file
    sequences=[]
    for read in SeqIO.parse(file, "fasta"):

        Uid=read.id.split("|")[-1]

        if Uid==n1 or Uid==n2:
            sequences.append(str(read.seq))

    if len(sequences)>=2:

        s1, s2, tr, scores=nw3(sequences[0], sequences[1], match, 1, match)##de que serveix eñ -4????? el ultim valor? match, mismatch? o que?

        score=scores[len(s1)-1][len(s2)-1] #bottom right corner for score

        return [score, s1, s2]
    else:
        return [0]
##-4 que es??
print(sequencereader("ppar.fasta", "PPARD_XENLA", "PPARG_CANLF", -4))
if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)
