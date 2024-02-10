
def knapsack(w, v, n, limw):
	'''
	>>> weights =  [7, 8, 3]
	>>> values =  [3000, 4000, 2000]
	>>> print(knapsack(weights, values, 3, 10))
	5000
	>>> weights =  [7, 8, 3]
	>>> values =  [3000, 6000, 2000]
	>>> print(knapsack(weights, values, 3, 10))
	6000
	>>> weights =  [1, 1, 1, 1]
	>>> values =  [3, 5, 7, 7]
	>>> print(knapsack(weights, values, 4, 2))
	14
	'''
	n_list = []
	sol, w, v = run_knapsack(w,v, n-1, limw,[],0)
	return sol
	
def run_knapsack(w, v, n, limw, n_list,c):
	if n == -1:
		total_value = sum([v[pos] for pos in n_list])
		return total_value, [w[pos] for pos in n_list], [v[pos] for pos in n_list]
		
	if sum([w[pos] for pos in n_list]) > limw:
		return 0, [], []
		
	include_value, include_weights, include_values = run_knapsack(w, v, n - 1, limw, n_list + [n],c)
	exclude_value, exclude_weights, exclude_values = run_knapsack(w, v, n - 1, limw, n_list,c)
	
	if sum(include_weights) <= limw:
		if sum(exclude_weights) <= limw:
			if include_value > exclude_value:
				return include_value, include_weights, include_values
			else:
				return exclude_value, exclude_weights, exclude_values
		else:
			return include_value, include_weights, include_values
	elif sum(exclude_weights) <= limw:
		return exclude_value, exclude_weights, exclude_values
		
	
weights =  [7, 8, 3]
values =  [3000, 4000, 2000]
print(f'\n\n{knapsack(weights, values, 3, 10)}')


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose = True)
