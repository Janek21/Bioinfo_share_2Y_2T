from pytokr import pytokr
item, items = pytokr(iter = True)

def quasi_minim(quantitat, n, monedes):
    M = [float('inf')]*(quantitat+1)
    M[0] = 0

    for i in range(n):
        for j in range(monedes[i], quantitat +  1):
            M[j] = min(M[j], M[j - monedes[i]] +  1)

    return M[quantitat] if M[quantitat] != float('inf') else 'no'


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