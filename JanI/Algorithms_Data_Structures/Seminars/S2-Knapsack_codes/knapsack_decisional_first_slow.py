"""
Slow knapsack by exhaustive search on powerset iterator, first solution

Jose L Balcazar, 2024, based on earlier files, maybe by others
"""

from powerset import powerset

def total(data, choices):
    return sum( data[i] for i in choices )

def slow_dec_knapsack(weights, values, last_item, max_w, min_v, placeholder, anotherplaceholder, yetanotherplaceholder):
    for cand in powerset(range(last_item + 1)):
        if total(weights, cand) <= max_w and total(values, cand) >= min_v:
            return cand
    return list()

