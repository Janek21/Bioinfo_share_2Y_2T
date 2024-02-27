def move_gaps_scores(seq1, seq2, match, mismatch, gap):
	"""
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
	"""
	
	# Ensure seq1 is the shorter sequence for simplicity
	seq1, seq2 = sorted([seq2, seq1], key=len)
	len_seq1, len_seq2 = len(seq1), len(seq2)

	# Initialize a list to store scores, starting with an empty string
	score = ['']

	# Print the second sequence as the reference sequence
	print(seq2)

	# Iterate through positions in seq1, including the case where there are no characters from seq1
	for x in range(len_seq1 + 1):
		# Create a new sequence with gaps to align with seq2
		new_seq = seq1[:x] + '-' * (len_seq2 - len_seq1) + seq1[x:]

		# Calculate the score for the alignment at the current position
		current_score = sum(match if new_seq[i] == seq2[i] else gap if new_seq[i] == '-' or seq2[i] == '-' else mismatch for i in range(len_seq2))

		# Append the current score to the list and print the alignment and score
		score.append(current_score)
		print(new_seq, current_score)

	return


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)

