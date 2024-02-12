def naive_match(p, t):
	
	'''
	>>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
	[3, 13, 21]
	>>> naive_match('FAST', 'FAST')
	[0]
	>>> naive_match('FASTA', 'FAST')
	[]
	'''
	
	
	lst = []

	for posicion in range(len(t) - len(p) + 1):
		coincide = True
		for letra in range(len(p)):
			if t[posicion + letra] != p[letra]:
				coincide = False
		if coincide:
			lst.append(posicion)
	return lst

if __name__ == "__main__":
		import doctest
		doctest.testmod(verbose=True)
