from pytokr import pytokr


def trace(best, goal):
	coins = []
	while goal:
		use = best[goal]
		coins.append(use)
		goal -= use
	return coins
	
def canvi(coin_list, maxsum):
	coin_list = [0] + coin_list
	table = {}
	best = {}
	for coin in coin_list:
		table[coin,0] = 0
	for subprob in range(maxsum+1):
		table[0,subprob] = float('inf')
		
	for subprob in range(1, maxsum+1):
		for coin in range(1, len(coin_list)):
			if coin_list[coin] <= subprob and 1+ table[coin_list[coin], subprob-coin_list[coin]] < table[coin_list[coin-1], subprob]:
				table[coin_list[coin], subprob] = 1+ table[coin_list[coin], subprob-coin_list[coin]]
				best[subprob] = coin_list[coin]
			else: table[coin_list[coin], subprob] = table[coin_list[coin-1], subprob]
	result_trace = trace(best, maxsum)
	return result_trace




item, items = pytokr(iter = True)

for case in items():
	goal = int(case)
	maxlist = []
	for _ in range(int(item())):
		maxlist.append(int(item()))
	
	maxlist = sorted([int(num) for num in maxlist])
	maxsum = sum(maxlist)
	
	box = [1, 2, 5, 10, 20, 50, 100, 200]
	
	result = sorted(canvi(box, maxsum))
	
	if maxlist == result:
		print('si')
	else: print('no')
	
