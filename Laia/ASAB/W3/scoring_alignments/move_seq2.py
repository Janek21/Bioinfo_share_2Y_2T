def move_seq2(seq1, seq2):
    '''
    >>> move_seq2("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT---------', 'THEFATCAT----------', '-THEFATCAT---------', '--THEFATCAT--------', '---THEFATCAT-------', '----THEFATCAT------', '-----THEFATCAT-----', '------THEFATCAT----', '-------THEFATCAT---', '--------THEFATCAT--', '---------THEFATCAT-', '----------THEFATCAT']
    >>> move_seq2("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT--------', 'AFASTCAT----------', '-AFASTCAT---------', '--AFASTCAT--------', '---AFASTCAT-------', '----AFASTCAT------', '-----AFASTCAT-----', '------AFASTCAT----', '-------AFASTCAT---', '--------AFASTCAT--', '---------AFASTCAT-', '----------AFASTCAT']
    '''

    res = [seq1+'-'*len(seq2)]
    dash = '-'*len(seq1)

    for i in range(len(seq1)+1):
        res.append(dash[:i] + seq2 + dash[i:])

    return res

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
