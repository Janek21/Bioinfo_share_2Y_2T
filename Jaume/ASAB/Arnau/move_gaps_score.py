def move_gaps(seq_1, seq_2):

	output = []
	long_seq = ""
	short_seq = ""
	dif = abs(len(seq_1) - len(seq_2))
	
	if len(seq_1) > len(seq_2):

		output.append(seq_1)
		long_seq = seq_1
		short_seq = seq_2
	
	else:

		output.append(seq_2)
		long_seq = seq_2
		short_seq = seq_1

	for i in range(len(long_seq) - dif + 1):
		
		output.append(short_seq[:i] + '-' * dif + short_seq[i:])

	return output

def score_seqs(seq_1, seq_2, match, mismatch, gap):

	score = 0
	
	if len(seq_1) != len(seq_2):
		return 0
	
	else:

		for i in range(len(seq_1)):

			if seq_1[i] == '-' or seq_2[i] == '-':
				score += gap

			elif seq_1[i] == seq_2[i]:
				score += match

			else:
				score += mismatch

	return score

def move_gaps_scores(seq_1, seq_2, match, missmatch, gap):
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
	
	if len(seq_1) > len(seq_2):
		long_seq = seq_1

	else: long_seq = seq_2

	print(long_seq)

	possible_alignments = move_gaps(seq_1, seq_2)
	
	for alignment in possible_alignments[1:]:

		score = score_seqs(long_seq, alignment, match, missmatch, gap)

		print(f'{alignment} {score}')

	return 0

if __name__ == "__main__":

	move_gaps_scores('THEFASTCAT', 'AFASTCAT', 1, -1, -2)

	print('')

	move_gaps_scores('AFASTCAT', 'THEFASTCAT', 1, -1, -2)

	'''
	import doctest
	doctest.testmod(verbose=True)
	'''
