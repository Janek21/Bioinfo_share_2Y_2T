def dot_matrix(seq1,seq2):
	l = []
	for x in range(len(seq1)):
		dot_plot = ['o' if seq1[pos] == seq2[x] else ' ' for pos in range(len(seq1))]
		l.append(dot_plot)
	return l

print( dot_matrix("FASTCAT", "TACTSAF"))

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose = True)
