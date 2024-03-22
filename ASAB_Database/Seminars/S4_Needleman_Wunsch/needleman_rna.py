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
    seq1, seq2, trace, scores=nw3(seq1, seq2, match, mismatch, gap) #collect outputs from nw
    return tracer(seq1, seq2, trace) #use tracer to construct the sequeces


if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)