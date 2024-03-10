from Bio import SeqIO

def count_matches_stars(fasta_file):
    '''
    >>> count_matches_stars("fastcats.fasta")
    '       ** * **'
    '''
    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Analyzing_a_sequence_alignment_(I)/' + fasta_file
    
    list_seqs = []
    
    for record in SeqIO.parse(file_path, 'fasta'):
        list_seqs.append(record)
    
    row = ''
    for i in range(len(list_seqs[1])):
        a = True
        for j in range(len(list_seqs)):
            if list_seqs[1][i] != list_seqs[j][i]:
                a = False
        if a == True:
            row += ('*')
        else:
            row += ' '
    
    return row

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
