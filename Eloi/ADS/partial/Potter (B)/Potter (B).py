from pytokr import pytokr

inp = pytokr()

def making_bowls(l, pos, candw, candv, maxw):
	
	# We Check if our accumated weight is bigger than the maximum permitted 
	if candw > maxw:
		return float('-inf') #Backtracking Step
		
	if pos == -1:
		if candw <= maxw:
			return candv
			
	option1 = making_bowls(l, pos - 1, candw, candv, maxw) # Option that moves on without taking
	option2 = making_bowls(l, pos - 1, candw + pos + 1, candv + l[pos], maxw) # Option that moves on while taking
	option3 = making_bowls(l, pos, candw + pos + 1, candv + l[pos], maxw) # Option that DOES NOT move on while taking
	
	return max(option1, option2, option3) 


reps = int(inp())
price_list=[]

for x in range(reps):
	inputed = inp()
	price_list.append(float(inputed)) 


result = making_bowls(price_list, len(price_list)-1, 0, 0, reps)
print("{:.2f}".format(result))
