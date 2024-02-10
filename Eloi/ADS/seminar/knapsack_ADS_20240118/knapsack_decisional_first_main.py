"""
Calling different ways of solving knapsack, first solution

Jose L Balcazar, 2024, based on earlier programs by several sources
"""

from pytokr import pytokr
from time import process_time

item = pytokr()

from knapsack_decisional_simple_first_no_back import knapsack as tree_knapsack
from knapsack_decisional_simple_first import knapsack as bt_knapsack
from knapsack_decisional_first_slow import slow_dec_knapsack 

# ~ for mxw in items(): # to run several cases at once
    # ~ mxw = int(mxw)

mnv = int(item())
mxw = int(item())
itq = int(item())
weights = []
values = []
for itm in range(itq):
    weights.append(int(item()))
    values.append(int(item()))
print("Powerset-based exhaustive search:")
start = process_time()
sol = slow_dec_knapsack(weights, values, itq - 1, mxw, mnv, [], 0, 0)
tm = process_time() - start
print(f"time: {1000*(tm):3.6f} ms")
print(sol, sum(values[e] for e in sol))
print("Tree-based exhaustive search:")
start = process_time()
sol = tree_knapsack(weights, values, itq - 1, mxw, mnv, [], 0, 0)
tm = process_time() - start
print(f"time: {1000*(tm):3.6f} ms")
print(sol, sum(values[e] for e in sol))
print("Backtracking scheme:")
start = process_time()
sol = bt_knapsack(weights, values, itq - 1, mxw, mnv, [], 0, 0)
tm = process_time() - start
print(f"time: {1000*(tm):3.6f} ms")
print(sol, sum(values[e] for e in sol))

