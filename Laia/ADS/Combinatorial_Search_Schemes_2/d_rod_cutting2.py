from pytokr import pytokr
item, items = pytokr(iter=True)

def rod_cut(prices, L):
    M = [[0 for _ in range(L+1)] for _ in range(len(prices)+1)]

    for i in range(1, len(prices)+1): # tall
        for j in range(1, L+1): # longitud barra
            if i <= j:
                M[i][j] = max(M[i-1][j], prices[i-1] + M[i][j-i])
            else:
                M[i][j] = M[i-1][j]

    return M[len(prices)][L]

L = int(item())
prices = []
for x in range(L):
    prices.append(float(item()))

print('{:.2f}'.format(rod_cut(prices, L)))
