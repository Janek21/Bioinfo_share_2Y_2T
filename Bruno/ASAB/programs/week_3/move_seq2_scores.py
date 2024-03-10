def move_seq2_scores(seq1, seq2, match, mismatch, gap):
    '''
    >>> move_seq2_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)
    THEFASTCAT--------
    AFASTCAT---------- -28
    -AFASTCAT--------- -28
    --AFASTCAT-------- -14
    ---AFASTCAT------- -29
    ----AFASTCAT------ -28
    -----AFASTCAT----- -29
    ------AFASTCAT---- -30
    -------AFASTCAT--- -33
    --------AFASTCAT-- -32
    ---------AFASTCAT- -35
    ----------AFASTCAT -36
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
    new_query = query + '-' * len(subject)

    for i in range(len(query) + 1):
        current_str = ''
        current_str = '-' * i + subject + '-' * (len(query) - i)
        count = 0
        for j in range(len(new_query)):
            if current_str[j] == '-' or new_query[j] == '-':
                count += gap
            elif current_str[j] == new_query[j]:
                count += match
            else:
                count += mismatch
        lista.append(current_str + ' ' + str(count))

    for x in lista:
        print(x)



print(move_seq2_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2))