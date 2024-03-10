def print_fasta(seqid_seq_dict):
    '''
    >>> print_fasta({'fast_cat': 'THEFASTCAT'})
    >fast_cat
    THEFASTCAT
    >>> print_fasta(read_fasta("thefastcat.fasta"))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(read_fasta("fastcats.fasta"))
    >FAST_CAT
    THE----FASTCAT
    >FAT_RAT
    THE----FA-TRAT
    >VERYFAST_CAT
    THEVERYFASTCAT
    >LAST_CAT
    ---LASTFA-TCAT
    >>> print_fasta({'many_cats': 'CAT' * 100})
    >many_cats
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    '''

    for key in seqid_seq_dict.keys():
        print('>' + key)
        #print(seqid_seq_dict[key])
        while seqid_seq_dict[key] != '':
            print(seqid_seq_dict[key][:60])
            seqid_seq_dict[key] = seqid_seq_dict[key][60:]
            
    return





def read_fasta(filename):

    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Parsing_a_FASTA_file/' + filename
    Dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            if line[0] == '>':
                key = line[1:].strip()
                Dict[key] = ''
            else:
                Dict[key] += line.strip()
    return Dict

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
