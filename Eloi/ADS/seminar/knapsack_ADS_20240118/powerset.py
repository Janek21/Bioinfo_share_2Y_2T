def powerset(iterable):
    "itertools recipe"
    from itertools import chain, combinations 
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
