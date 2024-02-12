def move_gaps(seq_1, seq_2):
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

    lst = []
    llarg = ""
    curt = ""
    gaps = abs(len(seq_1) - len(seq_2))
    
    if len(seq_1) > len(seq_2):

        lst.append(seq_1)
        llarg = seq_1
        curt = seq_2
    
    else:

        lst.append(seq_2)
        llarg = seq_2
        curt = seq_1

    for lletra in range(len(curt) + 1):
        
        lst.append(curt[:lletra] + '-' * gaps + curt[lletra:])

    return lst


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
