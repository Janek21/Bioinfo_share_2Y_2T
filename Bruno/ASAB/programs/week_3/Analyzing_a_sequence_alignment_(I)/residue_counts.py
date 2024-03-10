from Bio import SeqIO

def count_residue(fasta_file, residue):
    '''
    >>> count_residue("fastcats.fasta", "T")
    12
    >>> count_residue("fastcats.fasta", "A")
    9
    >>> count_residue("fastcats.fasta", "U")
    0
    >>> count_residue("fastcats.fasta", "")
    0
    '''

    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Analyzing_a_sequence_alignment_(I)/' + fasta_file
    seqs_list = []
    counter = 0
    
    for record in SeqIO.parse(file_path, 'fasta'):
        for x in record.seq:
            if residue == x:
                counter += 1
    
    return counter

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)