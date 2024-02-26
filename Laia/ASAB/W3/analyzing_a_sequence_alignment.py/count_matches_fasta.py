from Bio import SeqIO

def count_matches_fasta(fasta_file):
    '''
    >>> count_matches_fasta("cat_and_rat.fasta")
    8
    '''
    
    directory = '/home/laia/Desktop/ASAB/Week3/aa_material/'+fasta_file
    seqs = []
    for record in SeqIO.parse(directory, "fasta"):
        seqs.append(record.seq)
    
    c = 0
    for i in range(len(seqs[0])):
        if seqs[0][i] == seqs[1][i]:
             c += 1
    return c
        
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)