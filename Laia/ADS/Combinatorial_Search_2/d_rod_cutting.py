from pytokr import pytokr
item, items = pytokr(iter=True)

def rod_cut(prices, L):
    M = [[0 for _ in range(len(prices)+1)] for _ in range(L+1)]

    for i in range(1, L+1): # longitud barra
        for j in range(1, len(prices)+1): # tall
            if j <= i:
                M[i][j] = max(M[i][j-1], prices[j-1] + M[i-j][j])
            else:
                M[i][j] = M[i][j-1]

    return M[L][len(prices)]

L = int(item())
prices = []
for x in range(L):
    prices.append(float(item()))

print('{:.2f}'.format(rod_cut(prices, L)))
