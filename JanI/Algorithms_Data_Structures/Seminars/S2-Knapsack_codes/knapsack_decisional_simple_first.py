"""
Slow knapsack by simple backtracking, first solution

Jose L Balcazar, 2024, based on earlier files, maybe by others
"""


def knapsack(weights, values, current_item, max_w, min_v, cand, cand_w, cand_v, solutions):
	if current_item == -1:
		if cand_v >= min_v:
			return cand
		else:
			return list()
	else: 
		"current_item >= 0" 
		sol = knapsack(weights, values, current_item - 1, max_w, min_v, cand, cand_w, cand_v, solutions)
		if not sol and weights[current_item] <= max_w:
			sol = knapsack(weights, values, current_item - 1, 
					max_w - weights[current_item], min_v, 
					cand + [ current_item ], 
					cand_w + weights[current_item],
					cand_v + values[current_item], 
					solutions)
		if sol:
			solutions.append(sol)
			print(solutions)
		return sol

print(knapsack([1, 2, 1], [10, 20, 30], 2, 2, 11, [], 0, 0, []))

