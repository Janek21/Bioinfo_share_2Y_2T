def move_seq2(seq1, seq2):
    '''
    >>> move_seq2("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT---------', 'THEFATCAT----------', '-THEFATCAT---------', '--THEFATCAT--------', '---THEFATCAT-------', '----THEFATCAT------', '-----THEFATCAT-----', '------THEFATCAT----', '-------THEFATCAT---', '--------THEFATCAT--', '---------THEFATCAT-', '----------THEFATCAT']
    >>> move_seq2("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT--------', 'AFASTCAT----------', '-AFASTCAT---------', '--AFASTCAT--------', '---AFASTCAT-------', '----AFASTCAT------', '-----AFASTCAT-----', '------AFASTCAT----', '-------AFASTCAT---', '--------AFASTCAT--', '---------AFASTCAT-', '----------AFASTCAT']
    '''

    lista = []
    difference = 0
    if len(seq1) > len(seq2):
        subject = seq2
        query = seq1
        difference = len(seq1) - len(seq2)
        n = len(seq1) + len(seq2)
    elif len(seq1) < len(seq2):
        subject = seq1
        query = seq2
        difference = len(seq2) - len(seq1)
        n = len(seq1) + len(seq2)
    
    lista.append(query + '-' * len(subject))
    
    for i in range(len(query) + 1):
        lista.append('-' * i + subject + '-' * (len(query) - i))
    return lista

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
    