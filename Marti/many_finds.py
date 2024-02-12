def many_finds(p, t):
	'''
	>>> many_finds('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
	[3, 13, 21]
	>>> many_finds('FAST', 'FAST')
	[0]
	>>> many_finds('FASTA', 'FAST')
	[]
	'''
	
	lst = []
	score = t.find(p, 0)
	
	while score != -1:
		lst.append(score)
		score = t.find(p, score + 1)
	return lst
	
if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)

		
