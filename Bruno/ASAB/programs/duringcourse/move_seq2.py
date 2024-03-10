def move_seq2(seq1, seq2):
    '''
    >>> move_seq2("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT---------', 'THEFATCAT----------', '-THEFATCAT---------', '--THEFATCAT--------', '---THEFATCAT-------', '----THEFATCAT------', '-----THEFATCAT-----', '------THEFATCAT----', '-------THEFATCAT---', '--------THEFATCAT--', '---------THEFATCAT-', '----------THEFATCAT']
    >>> move_seq2("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT--------', 'AFASTCAT----------', '-AFASTCAT---------', '--AFASTCAT--------', '---AFASTCAT-------', '----AFASTCAT------', '-----AFASTCAT-----', '------AFASTCAT----', '-------AFASTCAT---', '--------AFASTCAT--', '---------AFASTCAT-', '----------AFASTCAT']
    
    '''
    result = []
    if len(seq1) > len(seq2):
        used = seq1
        main = seq2
    elif len(seq1) < len(seq2):
        used = seq2
        main = seq1
    
    result.append(used + '-' * len(main))

    n = len(seq1) + len(seq2)
    for i in range(len(main)+1):
        result.append('-' * i + main + '-' * (len(main)-i))
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)