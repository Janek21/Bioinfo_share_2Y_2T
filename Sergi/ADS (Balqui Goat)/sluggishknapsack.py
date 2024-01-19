def knapsack(weights, values, n, limw):
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
    def knapsack_recursive(index, remaining_weight):
        if index < 0 or remaining_weight <= 0:
            return 0, []

        
        value_excluded, items_excluded = knapsack_recursive(index - 1, remaining_weight)

        
        if weights[index] <= remaining_weight:
            value_included, items_included = knapsack_recursive(index - 1, remaining_weight - weights[index])
            value_included += values[index]

           
            if value_included > value_excluded:
                return value_included, items_included + [index]
        
  
        return value_excluded, items_excluded

    total_value, selected_items = knapsack_recursive(n - 1, limw)
    return selected_items


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)