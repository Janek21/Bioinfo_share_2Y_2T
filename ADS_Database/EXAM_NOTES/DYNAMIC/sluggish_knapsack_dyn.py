def knapsack(weights, values, n, limw):
    dp = [[0 for _ in range(limw + 1)] for _ in range(n + 1)]
    parent = [[None for _ in range(limw + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, limw + 1):
            if weights[i - 1] <= w:
                if values[i - 1] + dp[i - 1][w - weights[i - 1]] > dp[i - 1][w]:
                    dp[i][w] = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                    parent[i][w] = i - 1
                else:
                    dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
    print(parent)
    items = []
    w = limw
    for i in range(n, 0, -1):
        if parent[i][w] is not None:
            items.append(parent[i][w])
            w -= weights[parent[i][w]]


    return items
weights =  [7, 8, 3]
values =  [3000, 4000, 2000]
print(knapsack(weights, values, 3, 10))
