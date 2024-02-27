def dot_matrix(seq1,seq2, w=1, threshold = float('inf')):
	'''
	>>> dot_matrix("FASTCAT", "FATRAT", 4, 2)
    [['o', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'o', 'o', ' ', ' ', ' ', ' '], [' ', ' ', 'o', 'o', ' ', ' ', ' '], [' ', ' ', ' ', 'o', 'o', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'o', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'o']]
    >>> dot_matrix("FASTCAT", "FATRAT", 2, 4)
    A threshold smaller or equal than the window does not make sense
	'''
	if w == 0: print('Window should be 1 or larger');return
	if threshold <= w: print('A threshold smaller or equal than the window does not make sense'); return
	l = []
	so = sorted([seq1,seq2], key = len)
	for x in range(len(so[0])):
		dot_plot = ['o' if so[0][x:x+w] == so[1][pos:pos+w] or  and len(so[1]) - pos+1  > w and pos < threshold  else ' ' for pos in range(len(so[1]))]
		l.append(dot_plot)
	return l


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
