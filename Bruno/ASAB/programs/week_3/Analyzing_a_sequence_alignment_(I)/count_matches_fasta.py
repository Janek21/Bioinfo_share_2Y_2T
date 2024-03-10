from Bio import SeqIO
def count_matches_fasta(fasta_file):
    '''
    >>> count_matches_fasta("cat_and_rat.fasta")
    8
    '''
    
    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Analyzing_a_sequence_alignment_(I)/' + fasta_file
    
    list_seqs = []
    
    for record in SeqIO.parse(file_path, 'fasta'):
        list_seqs.append(record)
    
    counter = 0
    for i in range(len(list_seqs[1])):
        if list_seqs[0][i] == list_seqs[1][i]:
            counter += 1
    
    return counter

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
