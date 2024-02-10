
s = ['*', '-', 2, 8, '+', 4, 3]


def pref(L, pos):
	if pos >= len(L)-2:
		return L[pos]
	if not isinstance(L[pos], int) and isinstance(L[pos+1], int): 
		if L[pos] == '*':
			return pref(L[pos:], 0) * pref(L[pos:], 0)
		if L[pos] == '+':
			return pref(L[pos:], 0) + pref(L[pos:], 0)
		if L[pos] == '-':
			return pref(L[pos:], 0) - pref(L[pos:], 0)
	
	return L[pos]

print(pref(s,0))
