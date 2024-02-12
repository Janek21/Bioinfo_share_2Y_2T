from pytokr import pytokr
"""
Slow knapsack by simple backtracking, first solution

Jose L Balcazar, 2024, based on earlier files, maybe by others
"""
inp = pytokr()

def knapsack(weights, values, current_item, max_w, min_v, cand, cand_w, cand_v, lista):
    if current_item == -1:
        if cand_v >= min_v:
            lista.append(cand) 
        return

    # current_item >= 0
    knapsack(weights, values, current_item - 1, max_w, min_v, cand, cand_w, cand_v, lista)

    if weights[current_item] <= max_w:
        knapsack(weights, values, current_item - 1, max_w - weights[current_item], min_v,
                 cand + [current_item], cand_w + weights[current_item], cand_v + values[current_item], lista)


min_v = int(inp())
max_w = int(inp())
n_of_inps = int(inp())
weights = []
values = []
for _ in range(n_of_inps):
    weights.append(int(inp()))
    values.append(int(inp()))
solutions = []
current_item = len(weights)-1
cand_v = 0
cand_w = 0

knapsack(weights, values, current_item, max_w, min_v, [], cand_w, cand_v, solutions)

for x in solutions:
    print(*sorted(x))

