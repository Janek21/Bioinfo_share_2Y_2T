#!/usr/bin/python3

def move_seq2(seq1, seq2):
    '''
    >>> move_seq2("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT---------', 'THEFATCAT----------', '-THEFATCAT---------', '--THEFATCAT--------', '---THEFATCAT-------', '----THEFATCAT------', '-----THEFATCAT-----', '------THEFATCAT----', '-------THEFATCAT---', '--------THEFATCAT--', '---------THEFATCAT-', '----------THEFATCAT']
    >>> move_seq2("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT--------', 'AFASTCAT----------', '-AFASTCAT---------', '--AFASTCAT--------', '---AFASTCAT-------', '----AFASTCAT------', '-----AFASTCAT-----', '------AFASTCAT----', '-------AFASTCAT---', '--------AFASTCAT--', '---------AFASTCAT-', '----------AFASTCAT']
    '''
    if len(seq1)>len(seq2):
        long=seq1
        seq=seq2 #shorter seq is seq2
        ls=[long+"-"*len(seq), seq+"-"*len(long)] #largest in list is seq1 --- added
    else:
        long=seq2
        seq=seq1 #shorter seq is seq1
        ls=[long+"-"*len(seq), seq+"-"*len(long)] #largest in list is seq2 --- added
    
    for pos in range(len(long)):
        pos+=1
        front="-"*pos
        back="-"*(len(long)-pos)
        ls.append(front+seq+back)
    return ls

#print(move_seq2("THEFASTCAT", "THEFATCAT"))


if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)

