## RETORNA TOTES LES SOLUCIONS

from pytokr import pytokr
item, items = pytokr(iter = True)

def knapsack(weigths, values, n, max_w, min_v):
    M = [[0 for _ in range(max_w+1)] for _ in range(n+1)]
    best = [[False for _ in range(max_w+1)] for _ in range(n+1)]


    for i in range(1, n+1):
        for j in range(1, max_w+1):
            if weigths[i-1] <= j and values[i-1] + M[i-1][j - weigths[i-1]] > M[i-1][j]:
                M[i][j] = values[i-1] + M[i-1][j - weigths[i-1]]
                best[i][j] = True
            else: 
                M[i][j] = M[i-1][j]


    sol = []
    w, i = max_w, n
    while w > 0 and i >= 0:
        if best[w][i]:
            sol.append(i)
            w -= weigths[i]
        i -= 1
    return sol






min_v = int(item())
max_w = int(item())
n = int(item())
weigths = []
values = []
for i in range(n):
    weigths.append(int(item()))
    values.append(int(item()))

res = knapsack(weigths, values, n-1, max_w, min_v)
for x in res:
    print(*x)