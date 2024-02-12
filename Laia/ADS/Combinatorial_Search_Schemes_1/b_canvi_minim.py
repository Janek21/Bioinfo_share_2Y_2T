from pytokr import pytokr

item, items = pytokr(iter=True)

def canvi_minim(quantitat, valors_monedes, current_item, suma=0, monedes=[]):
    if current_item < 0:
        if suma == quantitat:
            return [monedes]
        return []
    else:
        m1 = canvi_minim(quantitat, valors_monedes, current_item - 1, suma, monedes)  # no agafas moneda

        m2, m3 = [], []
        if (suma + valors_monedes[current_item]) <= quantitat:
            m2 = canvi_minim(quantitat, valors_monedes, current_item - 1, 
                             suma + valors_monedes[current_item], monedes + [valors_monedes[current_item]])  # agafar moneda i canviar
            m3 = canvi_minim(quantitat, valors_monedes, current_item, 
                             suma + valors_monedes[current_item], monedes + [valors_monedes[current_item]])  # agafar moneda i no canviar

        return m1 + m2 + m3

while True:
    c = int(item()) # quantitat
    n = int(item()) # num monedes diferents
    lst = [] # valors monedes
    for x in range(n):
        i = int(item())
        lst.append(i)
    
    res = sorted(canvi_minim(c, lst, n - 1), key = len)
    if res:
        print(len(res[0]))
    else:
        print('no')

