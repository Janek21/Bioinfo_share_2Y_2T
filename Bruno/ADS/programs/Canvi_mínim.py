import sys

def min_coins(c, values):
    n = len(values)
    # Initialize the DP table
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (c + 1))

    # Fill the DP table
    for j in range(c + 1):
        dp[0][j] = float('inf')
    
    #try values
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if values[i - 1] <= j:
                dp[i][j] = min(1 + dp[i][j - values[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # If last value is infinite return no
    if dp[n][c] == float('inf'):
        return "no"
    
    return dp[n][c]

for line in sys.stdin:
    line = line.strip().split()
    print(line)
    c = int(line[0])
    values = list(map(int, line[2:]))
    print(min_coins(c, values))