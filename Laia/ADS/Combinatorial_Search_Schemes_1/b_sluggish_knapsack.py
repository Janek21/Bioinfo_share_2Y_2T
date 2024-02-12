def knapsack(weights, values, n, max_w):
    '''
    >>> weights =  [7, 8, 3]
    >>> values =  [3000, 4000, 2000]
    >>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
    5000
    >>> weights =  [7, 8, 3]
    >>> values =  [3000, 6000, 2000]
    >>> print(sum(values[obj] for obj in knapsack(weights, values, 3, 10)))
    6000
    >>> weights =  [1, 1, 1, 1]
    >>> values =  [3, 5, 7, 7]
    >>> print(sum(values[obj] for obj in knapsack(weights, values, 4, 2)))
    14
    '''
    sol, wei, val = _knapsack(weights, values, n-1, max_w)
    return sol


def _knapsack(weigths, values, current_item, max_w):
    if current_item == -1:
        return [], 0, 0
    else:
        sol1 = []
        sol0, wei0, val0 = _knapsack(weigths, values, current_item-1, max_w)
        if max_w-weigths[current_item] >= 0:
            sol1, wei1, val1 = _knapsack(weigths, values, current_item-1, max_w-weigths[current_item])
            wei1 += weigths[current_item]
            val1 += values[current_item]
            sol1 += [current_item]
        
        if sol1:
            if val0 > val1:
                return sol0, wei0, val0 
            else:
                return sol1, wei1, val1
        return sol0, wei0, val0 
         

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

