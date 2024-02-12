from pytokr import pytokr
item, items = pytokr(iter = True)

def knapsack(weights, values, current_item, max_w, min_v, cand = [], cand_w = 0, cand_v = 0):
    if current_item == -1:
        if cand_w <= max_w and cand_v >= min_v:
            return [cand]
        return []
    else:
        sol1 = knapsack(weights, values, current_item-1, max_w, min_v, cand, cand_w, cand_v)
        sol2 = knapsack(weights, values, current_item-1, max_w, min_v, 
                        cand + [current_item], cand_w + weights[current_item], cand_v + values[current_item])

        return sol1+sol2
        
min_v = int(item())
max_w = int(item())
n = int(item())
weigths = []
values = []
for i in range(n):
    weigths.append(int(item()))
    values.append(int(item()))

res = knapsack(weigths, values, n-1, max_w, min_v)
for x in res:
    print(*x)