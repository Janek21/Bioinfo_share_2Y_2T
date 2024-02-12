def knapsack(weights, values, n, limw):
    # Base case: if there are no objects or weight limit is 0
    if n == 0 or limw == 0:
        return []

    # If the weight of the nth object is more than the current weight limit,
    # then this object cannot be included in the knapsack
    if weights[n - 1] > limw:
        return knapsack(weights, values, n - 1, limw)

    # Otherwise, return the maximum of two cases:
    # 1. nth object included
    include_case = [n - 1] + knapsack(weights, values, n - 1, limw - weights[n - 1])

    # 2. nth object not included
    exclude_case = knapsack(weights, values, n - 1, limw)

    # Choose the case with the maximum total value
    if sum(values[i] for i in include_case) > sum(values[j] for j in exclude_case):
        return include_case
    else:
        return exclude_case

