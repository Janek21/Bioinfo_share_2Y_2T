"""
Slow knapsack by exhaustive search

Jose L Balcazar, 2023, based on earlier files, maybe by Ramon
"""


def total(data, choices):
    return sum( data[i] for i in choices )

def powerset(iterable):
    from itertools import chain, combinations # itertools recipe
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def slow_knapsack(weights, values, itq, limw):
  mx = 0
  best = None
  for cand in powerset(range(itq)):
    if total(weights, cand) <= limw:
      cmx = total(values, cand)
      if cmx > mx:
        best = cand
        mx = cmx
  return best, total(weights, best), total(values, best)

# ~ from pytokr import item, items
# ~ from pytokr import pytokr

# ~ item, items = pytokr(iter = True)

# ~ for mxw in items():
    # ~ mxw = int(mxw)
    # ~ itq = int(item())
    # ~ weights = []
    # ~ values = []
    # ~ for itm in range(itq):
        # ~ weights.append(int(item()))
        # ~ values.append(int(item()))
    # ~ sol = slow_knapsack(weights, values, itq, mxw)
    # ~ print(sol, sum(values[e] for e in sol))

