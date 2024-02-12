from pytokr import pytokr

def rod_cutting_dp(prices, n):
    # Initialize the table with zeros
    dp = [0] * (n +  1)

    # Iterate over the prices array
    for i in range(1, n +  1):
        max_value = float('-inf')
        # Iterate over all lengths from  1 to i
        for j in range(1, i +  1):
            # Update the table entry for the current length
            max_value = max(max_value, prices[j -  1] + dp[i - j])
        dp[i] = max_value

    # Return the maximum value for the full length of the rod
    print(dp)
    return dp[n]

item = pytokr()

n = int(item())
prices = []
for _ in range(n):
    prices.append(float(item()))
res = rod_cutting_dp(prices, n)
print('{:.2f}'.format(res))
