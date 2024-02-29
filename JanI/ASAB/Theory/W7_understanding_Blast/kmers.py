#!/usr/bin/python3

def kmers(sequence, size):
    '''
    >>> kmers("QLNFQLMSAGQLQ", 3)
    ['QLN', 'LNF', 'NFQ', 'FQL', 'QLM', 'LMS', 'MSA', 'SAG', 'AGQ', 'GQL', 'QLQ']
    >>> kmers("QLNFQLMSAGQLQ", 4)
    ['QLNF', 'LNFQ', 'NFQL', 'FQLM', 'QLMS', 'LMSA', 'MSAG', 'SAGQ', 'AGQL', 'GQLQ']
    '''
    kmers=[] #list to store kmers

    start=0 #set a strart position
    for end in range(size, len(sequence)+1): #iterate from size to end of sequence (including last character), iterate for the number of times equal to the difference of size to the end of the sequence
        kmers.append(sequence[start:end]) #append from the starting position to the end of the window, end= start+size
        start+=1 #add 1 to start, so the next window starts i character over
    
    return kmers

if __name__ == "__main__":

	import doctest
	doctest.testmod(verbose=True)