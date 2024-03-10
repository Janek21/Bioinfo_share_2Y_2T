def read_fasta(filename):
    '''
    >>> read_fasta('thefastcat.fasta')
    ('fast_cat', 'THEFASTCAT')
    '''
    path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Parsing_a_FASTA_file/' + filename
    with open(path, 'r') as file:
        for line in file:
            if line[0] == '>':
                a = (line[1:].strip(), '')
            else:
                new_second_element = str(a[1]) + line # Convert the second element to string and concatenate with '3'
                a = (a[0], new_second_element) # Create a new tuple with the modified second element

    return a

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)