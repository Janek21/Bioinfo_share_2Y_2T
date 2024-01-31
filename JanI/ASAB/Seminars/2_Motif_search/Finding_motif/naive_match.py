#!/usr/bin/python3

def naive_match(p, t):
    '''
    >>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> naive_match('FAST', 'FAST')
    [0]
    >>> naive_match('FASTA', 'FAST')
    []
    '''
    p_pos=[]
    for initial in range(len(t)):
        n=len(p)+initial #n is a number equal to our current position+ lenght of searched
        fragment=t[initial:n] #fragment is a piece of same length as p (from current position to current position+length of searched)
        if p==fragment: #if current fragment is searched add first position to list
            p_pos.append(initial)
    return(p_pos)

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)