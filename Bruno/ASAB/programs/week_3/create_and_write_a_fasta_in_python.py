def print_fasta(filename, seq):
    '''
    >>> print_fasta(('fast_cat', 'THEFASTCAT'))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(('', 'THEFASTCAT'))
    >unnamed
    THEFASTCAT
    >>> print_fasta(('', ''))
    '''
    if filename == '':
        filename = 'unnamed.fa'
    else:
        if '.fasta' not in filename:
            filename = filename + '.fasta'

    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Parsing_a_FASTA_file/' + filename


    #create file
    file = open(file_path, 'w')

    file.write('>' + filename + '\n')
    file.write(seq)
    
    file.close()

print_fasta('', 'ACGTCGTAAGTTC')
