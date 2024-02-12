
def move_seq2(seq1, seq2):
    '''
    >>> move_seq2("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT---------', 'THEFATCAT----------', '-THEFATCAT---------', '--THEFATCAT--------', '---THEFATCAT-------', '----THEFATCAT------', '-----THEFATCAT-----', '------THEFATCAT----', '-------THEFATCAT---', '--------THEFATCAT--', '---------THEFATCAT-', '----------THEFATCAT']
    >>> move_seq2("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT--------', 'AFASTCAT----------', '-AFASTCAT---------', '--AFASTCAT--------', '---AFASTCAT-------', '----AFASTCAT------', '-----AFASTCAT-----', '------AFASTCAT----', '-------AFASTCAT---', '--------AFASTCAT--', '---------AFASTCAT-', '----------AFASTCAT']
    '''
    lst = []
    
    full_seq = len(seq1) + len(seq2)
    
    gaps = '-' * full_seq
    
    lst.append(seq1 + '-' * len(seq2))
    
    for letra in range(len(seq1)+1):
        lst.append(gaps[0:letra] + seq2 + gaps[letra+len(seq2):])
    
    return lst
    
if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)
