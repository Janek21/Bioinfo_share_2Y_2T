#!/usr/bin/python3


def many_finds(p, t):
    '''
    >>> many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> many_finds('FAST', 'FAST')
    [0]
    >>> many_finds('FASTA', 'FAST')
    []
    '''
    result=[]
    result.append(t.find(p))
    
    for _ in range(len(result)+1): #las
        if result[-1]==-1: 
            return result[:-1]
        
        starter_pos=result[len(result)-1]+len(p) #start next search from end of word found in previous #[len(result)-1]=last_find
        result.append(t.find(p, starter_pos))
    
    return result

print(many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT'))


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)
