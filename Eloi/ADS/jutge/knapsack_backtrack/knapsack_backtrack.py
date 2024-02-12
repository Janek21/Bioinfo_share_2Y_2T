def knapsack(pos, weights, values, candw, candv, maxw):
	if candw > maxw:
		return float('-inf')
		
	if pos == -1:
		if candw <= maxw:
			return candv
	
	option1 = knapsack(pos-1, weights, values, candw + weights[pos], candv + values[pos], maxw)
	option2 = knapsack(pos-1, weights, values, candw, candv, maxw)
	
	return max(option1, option2)

weights =  [7, 8, 3]
values =  [3000, 6000, 2000]
print(knapsack(len(weights)-1, weights, values, 0, 0,10))

