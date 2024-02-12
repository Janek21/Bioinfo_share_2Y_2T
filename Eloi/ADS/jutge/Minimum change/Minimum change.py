from pytokr import pytokr

inp = pytokr()
def trace(best, goal, coin_list):
	coins = []
	while goal:
		use = best[goal]
		coins.append(use)
		goal -= use
	count_dic = {}
	for coin in coin_list[1:][::-1]:
		count_dic[coin] = 0
	for ent in coins:
		count_dic[ent] += 1
	return count_dic

def minimum(coin_list, main_obj):
	table = {}
	best = {}
	coin_list = [0] + coin_list
	for coin in coin_list:
		table[coin, 0] = 0
		best[coin] = 0
	for subobj in range(main_obj+1):
		table[0,subobj] = float('inf')

	for obj in range(1,main_obj+1):
		for coin in range(1, len(coin_list)):
			if coin_list[coin] <= obj and 1 + table[coin_list[coin], obj-coin_list[coin]] < table[coin_list[coin-1], obj]:
				table[coin_list[coin],obj] = 1 + table[coin_list[coin], obj-coin_list[coin]]
				best[obj] = coin_list[coin]
			else:
				table[coin_list[coin],obj] = table[coin_list[coin-1], obj]
	trace_result = trace(best, main_obj, coin_list)
	return table[coin_list[len(coin_list) - 1], main_obj], trace_result



obj_euros = int(inp())
obj_cents = int(inp())
coins_euros = [1,2,5, 10, 20, 50, 100, 200, 500]
coins_cents = [1, 2, 5, 10, 20, 50]


result_euros = minimum(coins_euros, obj_euros)
result_cents = minimum(coins_cents, obj_cents)
best_euros = result_euros[1]
best_cents = result_cents[1]

for coin in best_euros:
	if coin ==1:
		print(f'Coins of {coin} euro: {best_euros[coin]}')
	elif coin ==2:
		print(f'Coins of {coin} euros: {best_euros[coin]}')
	else: print(f'Banknotes of {coin} euros: {best_euros[coin]}')
for coin in best_cents:
	if coin == 1:
		print(f'Coins of {coin} cent: {best_cents[coin]}')
	else: print(f'Coins of {coin} cents: {best_cents[coin]}')
	

