from Bio import SeqIO


def count_matches_fasta(fasta_file):
	'''
    >>> count_matches_fasta("cat_and_rat.fasta")
    8
	'''
	
	fasta_path = '/home/marti/Baixades/material-20240123/cat_and_rat.fasta'
	fasta_file = open(fasta_path, 'r')

	count = 0
	sequences = list(SeqIO.parse(fasta_file, "fasta"))
	
	seq1 = str(sequences[0].seq)
	seq2 = str(sequences[1].seq)
	
	'''
	Optional:
	
	if len(seq1) != len(seq2):
		return("Invalid format: Sequences have different lengths")
	'''
	
	for letra in range(len(seq1)):
		if seq1[letra] == seq2[letra]:
			count += 1
	return count



if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)
