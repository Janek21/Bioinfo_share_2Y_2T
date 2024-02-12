from pytokr import pytokr
item, items = pytokr(iter = True)

def canvi_minim(quantitat, n, monedes):
    M = [float('inf')]*(quantitat+1)
    M[0] = 0

    for i in range(n):
        for j in range(monedes[i], quantitat +  1):
            M[j] = min(M[j], M[j - monedes[i]] +  1)

    return M[quantitat] if M[quantitat] < float('inf') else 'no'

 
while True:
    c = int(item()) # quantitat
    n = int(item()) # numero de diferents monedes
    lst = [] # valors de les monedes.
    for x in range(n): 
        i = int(item())
        lst.append(i)

    print(canvi_minim(c, n, lst))