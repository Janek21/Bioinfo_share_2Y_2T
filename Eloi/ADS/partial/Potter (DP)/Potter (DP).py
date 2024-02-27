from pytokr import pytokr

inp = pytokr()

def making_bowls(price_list, maxw):
	table = {} # Initiate table
	price_list = [0] + price_list
	
	#include wheights for every price ( price[0]: value / price[1]: weight )
	price_list = [[price_list[num],num] for num in range(len(price_list))]
	
	# Set table to be able to compare first First value 
	for weight in range(maxw+1): 
		table[0,weight] = 0 	
	for price in price_list:
		table[price[0], 0] = 0
		
	# Iterate over each cell using the Bellman equation to solve subproblems
	for weight in range(1,maxw+1):
		for price in range(1, len(price_list)):
			
			price_v = price_list[price][0] 
			price_w = price_list[price][1]
	
			if (price_w <= weight and 
			price_v + table[price_v, weight-price_w] > table[price_list[price-1][0], weight]):
				
				table[price_v,weight] = price_v + table[price_v, weight-price_w]
			
			else:
				table[price_v,weight] = table[price_list[price-1][0], weight]
				
	# Return last cell with last subproblem with answer
	return table[price_list[len(price_list) - 1][0], maxw] 	 


reps = int(inp())
price_list=[]
for x in range(reps):
	inputed = inp()
	price_list.append(float(inputed)) 


result = making_bowls(price_list,reps)
print("{:.2f}".format(result))

