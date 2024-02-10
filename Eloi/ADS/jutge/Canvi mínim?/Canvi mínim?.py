import sys

def canvi(l, pos, cands, candw, candv, maxw):
	print(cands)
	if candw > maxw:
		return float('-inf')
		
	if pos == -1:
		if candw <= maxw:
			return candv
		else:
			return float('-inf')
	
	option1 = canvi(l, pos - 1, cands, candw, candv, maxw)
	option2 = canvi(l, pos - 1, cands + [l[pos + 1]], candw + l[pos + 1], candv + l[pos], maxw)
	option3 = canvi(l, pos, cands + [l[pos + 1]], candw + l[pos + 1], candv + l[pos], maxw)
	
	return max(option1, option2, option3)


t = sys.stdin.readlines()

for x in t:
	max_sum = x[3:].strip().split(' ')
	max_sum = sum(int(num) for num in max_sum)
	
	box = [1, 2, 5, 10, 20, 50, 100, 200]

	result = canvi(box, len(box)-1, [], 0, 0, max_sum)
	print("{:.2f}".format(result))
