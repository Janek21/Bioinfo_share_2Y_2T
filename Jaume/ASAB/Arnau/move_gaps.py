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

    output = []
    long_seq = ""
    short_seq = ""
    dif = abs(len(seq_1) - len(seq_2))
    
    if len(seq_1) > len(seq_2):

        output.append(seq_1)
        long_seq = seq_1
        short_seq = seq_2
    
    else:

        output.append(seq_2)
        long_seq = seq_2
        short_seq = seq_1

    for i in range(len(short_seq) + 1):
        
        output.append(short_seq[:i] + '-' * dif + short_seq[i:])

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
