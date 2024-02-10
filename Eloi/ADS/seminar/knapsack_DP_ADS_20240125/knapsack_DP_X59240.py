"""
>>> weights =  [7, 8, 3]
>>> values =  [3000, 4000, 2000]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
5000
>>> weights =  [7, 8, 3]
>>> values =  [3000, 6000, 2000]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
6000
>>> weights =  [1, 1, 1, 1]
>>> values =  [3, 5, 7, 7]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 4, 2)))
14
>>> weights =  [1]
>>> values =  [1]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 1, 2)))
1
>>> weights =  [2, 1, 1, 1, 1]
>>> values =  [1, 1, 1, 1, 1]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 6)))
5
>>> weights =  [3, 2, 1, 1, 1]
>>> values =  [1, 1, 1, 1, 1]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 6)))
4
>>> weights = [9, 8, 12, 11, 7]
>>> values = [16, 15, 24, 23, 13]
>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 26)))
51
"""

def knapsack(weights, values, n, max_w):
	'''
	>>> weights =  [7, 8, 3]
	>>> values =  [3000, 4000, 2000]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
	5000
	>>> weights =  [7, 8, 3]
	>>> values =  [3000, 6000, 2000]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
	6000
	>>> weights =  [1, 1, 1, 1]
	>>> values =  [3, 5, 7, 7]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 4, 2)))
	14
	>>> weights =  [1]
	>>> values =  [1]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 1, 2)))
	1
	>>> weights =  [2, 1, 1, 1, 1]
	>>> values =  [1, 1, 1, 1, 1]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 6)))
	5
	>>> weights =  [3, 2, 1, 1, 1]
	>>> values =  [1, 1, 1, 1, 1]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 6)))
	4
	>>> weights = [9, 8, 12, 11, 7]
	>>> values = [16, 15, 24, 23, 13]
	>>> print(sum(values[obj] for obj in knapsack(weights, values, 5, 26)))
	51
	'''
	D = [[ 0 for _ in range(n) ] for _ in range(max_w + 1) ]
	best = [ [ False for _ in range(n) ] for _ in range(max_w + 1) ]
	
	for j in range(n):
		"init for zero weight: best and only option empty knapsack"
		D[0][j] = 0
	for j in range(n):
		for w in range(1, max_w + 1): 
			"update matrices at that cell"
			if D[w - weights[j]][j-1] + values[j] > D[w][j-1] and weights[j] <= w:
				"best is to take object j in"
				D[w][j] = D[w - weights[j]][j-1] + values[j]
				best[w][j] = True
			else:
				"best is not to take it"
				D[w][j] = D[w][j-1]

	sol = list() # trace the solution
	w, i = max_w, n - 1
	while w > 0 and i >= 0:
		if best[w][i]:
			sol.append(i)
			w -= weights[i]
		i -= 1
	return sol # take second value (and comma) out for testmod and Jutge

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose = True)


