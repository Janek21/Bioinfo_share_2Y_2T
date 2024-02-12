from pytokr import pytokr
item, items = pytokr(iter = True)

def rod_cut(prices, current_item, length, value):
    if current_item == -1:
        return value
    else:
        s1 = rod_cut(prices, current_item-1, length, value) # no tallar

        s2 = 0
        s3 = 0
        if length >= current_item:
            s2 = rod_cut(prices, current_item-1, length-(current_item+1), value + prices[current_item]) # tallar i canviar
            s3 = rod_cut(prices, current_item, length-(current_item+1), value + prices[current_item]) # tallar i no canviar
        
        return max(s1, s2, s3)


L = int(item())
prices = []
for x in range(L):
    prices.append(float(item()))

print('{:.2f}'.format(rod_cut(prices, L-1, L-1, 0.0)))
