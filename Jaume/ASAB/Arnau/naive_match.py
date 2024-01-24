def naive_match(p, t):
	'''
    >>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> naive_match('FAST', 'FAST')
    [0]
    >>> naive_match('FASTA', 'FAST')
    []
	'''

	output = []

	for i in range(len(t)):

		if t[i : i + len(p)] == p:

			output.append(i)

		# print(t[i : i + len(p)])
		
	return(output)

if __name__ == "__main__":
	'''
	naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')

	print()

	naive_match('FAST', 'FAST')

	print()

	naive_match('FASTA', 'FAST')
	'''
	
	import doctest
	doctest.testmod(verbose=True)
	