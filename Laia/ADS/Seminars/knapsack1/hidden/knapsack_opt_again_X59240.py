"""
Opt knapsack by backtracking

Jose L Balcazar, 2024, based on earlier files, maybe by others
"""

def _knapsack(weights, values, current_item, max_w):
	if current_item == -1:
		return ([],0,0)
	else: 
		"current_item >= 0" 
		best0, bestw0, bestv0 = _knapsack(weights, values, current_item - 1, max_w)
		if weights[current_item] <= max_w:
			best1, bestw1, bestv1 = _knapsack(
				weights, values, current_item - 1, max_w - weights[current_item])
			if bestv1 + values[current_item] > bestv0:
				best1.append(current_item)
				return best1, bestw1 + weights[current_item], bestv1 + values[current_item]
	return best0, bestw0, bestv0

def knapsack(weights, values, n, max_w):
	sol, wei, val = _knapsack(weights, values, n-1, max_w)
	return sol

