from pytokr import pytokr
item, items = pytokr(iter=True)

def potter(prices, L):
    dp = [0]*(L+1)

    for i in range(1, L+1):
        max_val = float('-inf')
        for j in range(1, i+1):
            max_val = max(max_val, prices[j-1] + dp[i-j])
        dp[i] = max_val
            
    return dp[-1]

L = int(item())
prices = []
for x in range(L):
    prices.append(float(item()))

print('{:.2f}'.format(potter(prices, L)))
