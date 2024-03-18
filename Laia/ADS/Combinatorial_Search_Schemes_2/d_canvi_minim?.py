from pytokr import pytokr
item, items = pytokr(iter = True)

def minim(quantitat, n, monedes):
    M = [[0 for _ in range(quantitat+1)] for _ in range(len(monedes)+1)]

    for j in range(quantitat+1):
        M[0][j] = float('inf')

    for i in range(1, len(monedes)+1): # monedes
        for j in range(1, quantitat+1):
            if monedes[i-1] <= j:
                M[i][j] = min(M[i-1][j], 1 + M[i][j-monedes[i-1]])
            else:
                M[i][j] = M[i-1][j]

    if M[n][quantitat] < float('inf'):
        return M[len(monedes)][quantitat]
    return 'no'


for x in items():
    mon =  [1, 2, 5, 10, 20, 50, 100, 200]
    monedes = []

    for i in range(int(x)):
        monedes.append(int(item()))

    res = minim(sum(monedes), int(x), mon)
    comp = len(monedes)

    if res == comp:
        print('si')
    else:
        print('no')