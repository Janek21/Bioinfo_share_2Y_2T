def move_gaps(seq1, seq2):
    '''
    >>> move_gaps("THEFASTCAT", "THEFATCAT")
    ['THEFASTCAT', '-THEFATCAT', 'T-HEFATCAT', 'TH-EFATCAT', 'THE-FATCAT', 'THEF-ATCAT', 'THEFA-TCAT', 'THEFAT-CAT', 'THEFATC-AT', 'THEFATCA-T', 'THEFATCAT-']
    >>> move_gaps("THEFASTCAT", "AFASTCAT")
    ['THEFASTCAT', '--AFASTCAT', 'A--FASTCAT', 'AF--ASTCAT', 'AFA--STCAT', 'AFAS--TCAT', 'AFAST--CAT', 'AFASTC--AT', 'AFASTCA--T', 'AFASTCAT--']
    >>> move_gaps("THEFATCAT", "THEFASTCAT")
    ['THEFASTCAT', '-THEFATCAT', 'T-HEFATCAT', 'TH-EFATCAT', 'THE-FATCAT', 'THEF-ATCAT', 'THEFA-TCAT', 'THEFAT-CAT', 'THEFATC-AT', 'THEFATCA-T', 'THEFATCAT-']
    >>> move_gaps("AFASTCAT", "THEFASTCAT")
    ['THEFASTCAT', '--AFASTCAT', 'A--FASTCAT', 'AF--ASTCAT', 'AFA--STCAT', 'AFAS--TCAT', 'AFAST--CAT', 'AFASTC--AT', 'AFASTCA--T', 'AFASTCAT--']
    '''

    lista = []
    difference = 0
    if len(seq1) > len(seq2):
        subject = seq2
        query = seq1
        difference = len(seq1) - len(seq2)
    elif len(seq1) < len(seq2):
        subject = seq1
        query = seq2
        difference = len(seq2) - len(seq1)
    
    lista.append(query)

    for i in range(len(subject)+1):
        lista.append(subject[:i] + '-' * difference + subject[i:])
    
    return lista

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)