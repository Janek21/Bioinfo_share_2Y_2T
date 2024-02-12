def print_fasta(filename):
	'''
	>>> print_fasta(('fast_cat', 'THEFASTCAT'))
	>fast_cat
	THEFASTCAT
	>>> print_fasta(('', 'THEFASTCAT'))
	>unnamed
	THEFASTCAT
	>>> print_fasta(('', ''))
	'''
	
	
	sequence_id, sequence = filename
	
	
	if not sequence_id:
		sequence_id = 'unnamed'
		
	if not sequence:
		return
	
	print(f">{sequence_id}\n{sequence}")
	
	
if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)

