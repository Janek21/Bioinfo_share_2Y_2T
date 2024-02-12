from Bio import SeqIO


def read_fasta(filename):
	'''
	>>> read_fasta('thefastcat.fasta')
	('fast_cat', 'THEFASTCAT')
	'''
	
	fasta_path = '/home/marti/Baixades/material-20240123/thefastcat.fasta'
	fasta_file = open(fasta_path, 'r')


	lines = fasta_file.readlines()
	sequence_id = lines[0].strip().replace('>', '')
	sequence = lines[1].strip()

	return sequence_id, sequence



if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)

