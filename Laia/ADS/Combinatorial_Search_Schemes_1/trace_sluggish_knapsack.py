def knapsack(weights, values, n, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    best = [[None for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j and dp[i-1][j] < values[i-1]+dp[i-1][j-weights[i-1]]:
                dp[i][j] = values[i-1]+dp[i-1][j-weights[i-1]]
                best[i][j] = i-1
            else:
                dp[i][j] = dp[i-1][j]

    res = []
    w = capacity
    for i in range(n, 0, -1):
        if best[i][w] is not None:
            res.append(best[i][w])
            w -= weights[best[i][w]]
    return res

print(knapsack([7, 8, 3], [3000, 4000, 2000], 3, 10))