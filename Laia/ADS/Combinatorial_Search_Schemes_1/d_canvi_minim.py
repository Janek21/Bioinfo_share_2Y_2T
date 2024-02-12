from pytokr import pytokr
item, items = pytokr(iter = True)

def canvi_minim(quantitat, n, monedes):
    M = [[0 for _ in range(quantitat+1)] for _ in range(n+1)]

    for i in range(n+1):
        M[i][0] = 0
    
    for j in range(quantitat+1):
        M[0][j] = float('inf')

    for i in range(1, n+1):
        for j in range(1, quantitat+1):
            if monedes[i-1] <= j:
                M[i][j] = min(M[i-1][j], 1 + M[i][j-monedes[i-1]])
            else:
                M[i][j] = M[i-1][j]

    if M[n][quantitat] < float('inf'):
        return M[n][quantitat]
    return 'no'
 
while True:
    c = int(item()) # quantitat
    n = int(item()) # numero de diferents monedes
    lst = [] # valors de les monedes.
    for x in range(n): 
        i = int(item())
        lst.append(i)

    print(canvi_minim(c, n, lst))