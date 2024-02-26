#!/usr/bin/python3

from needleman3 import nw3

def tracer(seq1, seq2, trace): #reconstruct seq using tracing matrix
    
    aln_seq1=[]
    aln_seq2=[]

    i=len(seq1)
    j=len(seq2)

    while i>0 or j>0:   
        #detect if insertion, deletion or substitution
        if trace[i][j]==0: #substitution, no added or remove
            aln_seq1.append(seq1[i-1])
            aln_seq2.append(seq2[j-1])

            #as its 0 you move in diagonal, so you reduce i and j
            i-=1
            j-=1

        elif trace[i][j]==-1: #insertion, we add gap in shorter seq
            aln_seq1.append("-")
            aln_seq2.append(seq2[j-1])

            #move to previous column, we reduce by 1 only the column position
            j-=1

        else: #deletion, we remove the nucleotide that should have been in position i, j of longer sequence by not adding it
            aln_seq1.append(seq1[i-1])
            aln_seq2.append("-")

            #move to previous row, we use the same method as before, we reduce by 1 only the row position
            i-=1
  
    #we moved from back to front in the matrix, we reorder the seq by reversing it
    aln_seq1.reverse()
    aln_seq2.reverse()

    return "".join(aln_seq1), "".join(aln_seq2)


def nw(seq1, seq2, match, mismatch, gap):
    '''
    >>> nw('ATCGATGCTATGCTAAATACGAT', 'UCGAUGCUAUCUAAAUAACGAU', 1, -8, -4)
    ('ATCGATGCTATGCTAAA-TACGAT', '-UCGAUGCUA-UCUAAAUAACGAU')
    >>> nw('UCGAUGCUAUCUAAAUAACGAU', 'ATCGATGCTATGCTAAATACGAT', 1, -8, -4)
    ('-UCGAUGCUA-UCUAAAUAACGAU', 'ATCGATGCTATGCTAAA-TACGAT')
    '''
    seq1, seq2, trace, scores=nw3(seq1, seq2, match, mismatch, gap)
    return tracer(seq1, seq2, trace)

if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)

####################################################################################################################
    
def translator(seq, pos): # to use translated rna seq
    if pos>=len(seq):
        return "".join(seq)
    if seq[pos]=="U":
        seq[pos]="T"
    return translator(seq, pos+1)

def detranslator(seq, pos):
    if pos>=len(seq):
        return "".join(seq)
    if seq[pos]=="T":
        seq[pos]="U"
    return detranslator(seq, pos+1)

def nw_rna(seq1, seq2, match, mismatch, gap):

    #aligning using traslated rna sequence
    rna=""
    if "U" in seq1:
        seq1=translator(list(seq1), 0)
        rna=seq1
    elif "U" in seq2:
        seq2=translator(list(seq2), 0)
        rna=seq2

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

            if seq1[i-1]==seq2[j-1]: #compare all nucleotides in seq1 vs the ones in seq2 (the -1 is because we begin in pos1 and end in +1)
                score=match #if the nucleotides are the same in both sequences define score as match

            else:
                score=mismatch #if they are different define score as mismatch
            
            #calculate the score for a insertion, deletion or substitution
            sb=M[i-1][j-1]+score
            ins= M[i][j-1]+gap
            delet=M[i-1][j]+gap

            if sb>=ins and sb>=delet:
                M[i][j]=sb
                trace[i][j]=0 #point in to the current point

            elif ins>=delet:
                M[i][j]=ins
                trace[i][j]=-1 #point to previous column (left)
            
            else:
                M[i][j]=delet
                trace[i][j]=1 #point to the previous row (up)

    #detreanslating RNA sequences for output

    if rna==seq1:
        seq1=detranslator(list(seq1), 0)

    elif rna==seq2:
        seq2=detranslator(list(seq2), 0)

    return tracer(seq1, seq2, trace)