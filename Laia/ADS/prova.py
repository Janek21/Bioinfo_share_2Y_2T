from pytokr import pytokr
item, items = pytokr(iter = True)

def canvi_minim(c, n, monedes):
    dp = [[float('inf') for _ in range(c+1)] for _ in range(n+1)]
    best = [[None for _ in range(c+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            if monedes[i-1] <= j and 1+dp[i][j-monedes[i-1]] < dp[i-1][j]:
                dp[i][j] = 1+dp[i][j-monedes[i-1]]
                best[i][j] = i-1
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][c]
 
while True:
    c = int(item()) # quantitat
    n = int(item()) # numero de diferents monedes
    lst = [] # valors de les monedes.
    for x in range(n): 
        i = int(item())
        lst.append(i)

    print(canvi_minim(c, n, lst))