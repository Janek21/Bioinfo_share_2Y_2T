from pytokr import pytokr

inp = pytokr()

def cutting(l, pos, cands, candw, candv, maxw):
	
	if candw > maxw:
		return float('-inf')
		
	if pos == -1:
		if candw <= maxw:
			return candv
		else:
			return float('-inf')
			
	option1 = cutting(l, pos - 1, cands, candw, candv, maxw)
	option2 = cutting(l, pos - 1, cands + [pos + 1], candw + pos + 1, candv + l[pos], maxw)
	option3 = cutting(l, pos, cands + [pos + 1], candw + pos + 1, candv + l[pos], maxw)
	
	return max(option1, option2, option3)


reps = int(inp())
price_list=[]
for x in range(reps):
	inputed = inp()
	price_list.append(float(inputed)) 


result = cutting(price_list, len(price_list)-1, [], 0, 0, reps)
print("{:.2f}".format(result))
