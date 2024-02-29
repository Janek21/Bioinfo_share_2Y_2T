#!/usr/bin/python3
import os

os.chdir("/home/jj/Desktop/Bioinformatics/2nd_year/2term/ASAB/Theory/W7_understanding_Blast")

from Bio.Align import substitution_matrices
from needleman_substmat import nw as substmat_calculator
from kmers import kmers

substitution_matrices.load("BLOSUM62")

def score_words(kmer_list):
    '''
    >>> score_words(['AAA', 'AAS', 'ASA', 'SSA', 'SSS'])
    {'AAA': [(12.0, 'AAA'), (9.0, 'ASA'), (9.0, 'AAS'), (6.0, 'SSA'), (3.0, 'SSS')], 'AAS': [(12.0, 'AAS'), (9.0, 'AAA'), (6.0, 'SSS'), (6.0, 'ASA'), (3.0, 'SSA')], 'ASA': [(12.0, 'ASA'), (9.0, 'SSA'), (9.0, 'AAA'), (6.0, 'SSS'), (6.0, 'AAS')], 'SSA': [(12.0, 'SSA'), (9.0, 'SSS'), (9.0, 'ASA'), (6.0, 'AAA'), (3.0, 'AAS')], 'SSS': [(12.0, 'SSS'), (9.0, 'SSA'), (6.0, 'ASA'), (6.0, 'AAS'), (3.0, 'AAA')]}
    >>> score_words(kmers("QLNFQLMSAGQLQ", 10))
    {'QLNFQLMSAG': [(49.0, 'QLNFQLMSAG'), (-8.0, 'NFQLMSAGQL'), (-13.0, 'LNFQLMSAGQ'), (-15.0, 'FQLMSAGQLQ')], 'LNFQLMSAGQ': [(49.0, 'LNFQLMSAGQ'), (-3.0, 'FQLMSAGQLQ'), (-13.0, 'QLNFQLMSAG'), (-13.0, 'NFQLMSAGQL')], 'NFQLMSAGQL': [(49.0, 'NFQLMSAGQL'), (-8.0, 'QLNFQLMSAG'), (-12.0, 'FQLMSAGQLQ'), (-13.0, 'LNFQLMSAGQ')], 'FQLMSAGQLQ': [(48.0, 'FQLMSAGQLQ'), (-3.0, 'LNFQLMSAGQ'), (-12.0, 'NFQLMSAGQL'), (-15.0, 'QLNFQLMSAG')]}
    '''
    sol={}
    for kmer_main in kmer_list:
        sol[kmer_main]=[]

        for kmer_compared in kmer_list:

            score, seq1, seq2=substmat_calculator(kmer_main, kmer_compared, 0) ##gap breaks things

            sol[kmer_main].append((score, kmer_compared))

    return sol
    
def scorer(kmer_i, kmer_j): ##finish

    subst_mat = substitution_matrices.load("BLOSUM62")

    M=[[0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    trace=[[0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]


    for h_line in range(1,len(seq1)+1):

        M[h_line][0]=gap*h_line
        trace[h_line][0]=1 #point up (up 1 position (+1 in column))

    for v_line in range(1,len(seq2)+1):

        M[0][v_line]=gap*v_line
        trace[0][v_line]=-1 #point left (back 1 position(-1 in row))
    
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            #i-1 and j-1 are used because we are iterating from 1 to len+1, so i, j would not cover all seq positions
            #we use this range to cover the margins with the tracing matrix

            score = subst_mat[seq1[i-1], seq2[j-1]]#get score from score matrix instead of getting it from input
            
            #calculate the score for a insertion, deletion or substitution
            sb=M[i-1][j-1]+score
             


if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)