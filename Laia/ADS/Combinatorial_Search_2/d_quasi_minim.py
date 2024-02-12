from pytokr import pytokr
item, items = pytokr(iter = True)

def quasi_minim(quantitat, n, monedes):
    M = [[0 for _ in range(quantitat+1)] for _ in range(n+1)]

    for j in range(quantitat+1):
        M[0][j] = float('inf')

    for i in range(1, n+1): # monedes
        for j in range(1, quantitat+1):
            if monedes[i-1] <= j:
                M[i][j] = min(M[i-1][j], 1 + M[i][j-monedes[i-1]])
            else:
                M[i][j] = M[i-1][j]
    if M[n][quantitat] < float('inf'):
        return M[n][quantitat]
    return 'no'


for x in items():
    monedes = []
    for i in range(int(x)):
        monedes.append(int(item()))
    mon =  [1, 2, 5, 10, 20, 50, 100, 200]
    n = len(mon)
    res = quasi_minim(sum(monedes), n, mon)
    comp = len(monedes)
    if res == comp or comp == res+1:
        print('si')
    else:
        print('no')