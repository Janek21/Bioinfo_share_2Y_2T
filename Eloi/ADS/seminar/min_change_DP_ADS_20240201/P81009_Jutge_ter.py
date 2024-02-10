
from pytokr import pytokr

def minchange(goal, denoms):
	'''
	>>> minchange(0, (10000,))
	0
	>>> minchange(1000, (1000, 600, 400))
	1
	>>> minchange(20, (17, 6, 4, 2))
	4
	>>> minchange(15, (17, 6, 4, 2))
	-1
	>>> minchange(5, (1, 2, 3))
	2
	'''
	dptable = [ float("inf") ] * (goal + 1)
	dptable[0] = 0
	best = {}
	for quant in range(1, goal+1):
		'''
		dptable[quant]: how many coins to add up to it
		'''
		for coin in denoms:
			"try using it"
			if coin <= quant:
				dptable[quant] = min(dptable[quant], 1 + dptable[quant - coin])
				
	
	return -1 if dptable[goal] > goal else dptable[goal]

item, items = pytokr(iter = True)

for case in items():
	goal = int(case)
	denoms = []
	for _ in range(int(item())):
		"statement guarantees at least one"
		denoms.append(int(item()))
	r = minchange(goal, denoms)
	if r == -1:
		print("no")
	else:
		print(r)


