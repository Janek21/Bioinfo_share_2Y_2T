from move_gaps import move_gaps
from score_seqs_gaps import score_seqs

def move_gaps_scores(seq1, seq2, match, mismatch, gap):
	'''
	>>> move_gaps_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)
	THEFASTCAT
	--AFASTCAT 2
	A--FASTCAT 2
	AF--ASTCAT 0
	AFA--STCAT -2
	AFAS--TCAT -4
	AFAST--CAT -6
	AFASTC--AT -8
	AFASTCA--T -10
	AFASTCAT-- -12
	>>> move_gaps_scores('AFASTCAT', 'THEFASTCAT', 1, -1, -2)
	THEFASTCAT
	--AFASTCAT 2
	A--FASTCAT 2
	AF--ASTCAT 0
	AFA--STCAT -2
	AFAS--TCAT -4
	AFAST--CAT -6
	AFASTC--AT -8	
	AFASTCA--T -10
	AFASTCAT-- -12
	'''
	

	alignments = move_gaps(seq1, seq2)
		
	print(alignments[0])
		
	for palabra in alignments[1:]:	
		result = score_seqs(alignments[0], palabra, match, mismatch, gap)
		print(f'{palabra} {result}')




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
