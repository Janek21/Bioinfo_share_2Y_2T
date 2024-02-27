from pytokr import pytokr
inp = pytokr()

results = []
def check_straigths(L,i,j):
	print(f'i: {i} / j:{j}')
	for check_i in range(len(L)):
		if L[check_i][j] == 'Q':
			return True
	for check_j in range(len(L)):
		if L[i][check_j] == 'Q':
			return True
	return False
	

def check_diagonal(L,i,j):
	for check in range(len(L)-1):
		if L[i-check][j-check] == 'Q':
			return True
	for check in range(len(L)-1):
		if L[i-check][-j+check] == 'Q':
			return True
	return False
			
def queens(L,i,j):
	if j >= len(L):
		if i >= len(L)-1:
			results.append([row.copy() for row in L])
			return
		queens(L,i+1,0)
		return
		
	hits_s = check_straigths(L,i,j)
	hits_d = check_diagonal(L,i,j)

	if not (hits_s+hits_d):
		L[i][j] = 'Q'
		queens(L,i,j+1)
		L[i][j] = '.'
	queens(L,i,j+1)
	return
	
	
reps = int(inp())
empty_matrix = [['.' for repX in range(reps)] for repY in range(reps)]
queens(empty_matrix, 0, 0)
for x in results:
	print(f'\n\n')
	for y in x:
		print(' '.join(y))
