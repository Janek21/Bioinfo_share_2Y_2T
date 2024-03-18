from pytokr import pytokr
item, items = pytokr(iter = True)

def canvi_minim(q):
    monedes = [1, 2, 5, 10, 20, 50, 100, 200]
    i = len(monedes)-1
    res = []
    while q > 0:
        while q >= monedes[i] and i >= 0:
            res.append(monedes[i])
            q -= monedes[i]
        i -= 1
    return len(res)
    
    
for n in items():
    n = int(n)
    lst = []
    for x in range(n):
        x = int(item())
        lst.append(x)
    quantitat = sum(lst)

    result = canvi_minim(quantitat)
    initial = len(lst)

    if result < initial-1:
        print('no')
    else:
        print('si')
