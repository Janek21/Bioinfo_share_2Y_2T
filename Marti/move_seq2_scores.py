from move_seq2 import move_seq2
from score_seqs_gaps import score_seqs

def move_seq2_scores(seq1, seq2, match, mismatch, gap):
	'''
    >>> move_seq2_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)
    THEFASTCAT--------
    AFASTCAT---------- -28
    -AFASTCAT--------- -28
    --AFASTCAT-------- -14
    ---AFASTCAT------- -29
    ----AFASTCAT------ -28
    -----AFASTCAT----- -29
    ------AFASTCAT---- -30
    -------AFASTCAT--- -33
    --------AFASTCAT-- -32
    ---------AFASTCAT- -35
    ----------AFASTCAT -36

	'''
	
	alignments = move_seq2(seq1, seq2)
		
	print(alignments[0])
		
	for palabra in alignments[1:]:	
		result = score_seqs(alignments[0], palabra, match, mismatch, gap)
		print(f'{palabra} {result}')


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
