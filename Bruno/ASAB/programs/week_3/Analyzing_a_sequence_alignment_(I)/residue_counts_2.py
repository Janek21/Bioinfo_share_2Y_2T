from Bio import SeqIO

def have_residue(fasta_file, residue, mincount):
    '''
    >>> have_residue("fastcats.fasta", "E", 2)
    1
    >>> have_residue("fastcats.fasta", "T", 2)
    4
    >>> have_residue("fastcats.fasta", "W", 0)
    4
    >>> have_residue("fastcats.fasta", "W", 1)
    0
    >>> have_residue("fastcats.fasta", "", 1)
    0
    '''

    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Analyzing_a_sequence_alignment_(I)/' + fasta_file
    result_counter = 0
    for record in SeqIO.parse(file_path, 'fasta'):
        counter = 0
        for x in record.seq:
            if x == residue:
                counter += 1
        if counter >= mincount:
            result_counter += 1
    
    return result_counter

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)