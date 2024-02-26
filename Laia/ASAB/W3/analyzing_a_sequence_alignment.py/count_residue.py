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
    directory = '/home/laia/Desktop/ASAB/Week3/aa_material/'+fasta_file
    records = SeqIO.parse(directory, 'fasta')
    if residue == "":
        return 0
    count  = 0
    return sum(record.seq.count(residue) for record in records)
    
##ARNAU

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)