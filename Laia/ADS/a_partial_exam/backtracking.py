from pytokr import pytokr
item, items = pytokr(iter = True)

def potter(prices, current_item, length, value):
    if current_item == -1:
        return value
    else:
        s1 = potter(prices, current_item-1, length, value) 

        s2, s3 = 0, 0
        if length >= current_item:
            s2 = potter(prices, current_item-1, length-(current_item+1), value + prices[current_item]) 
            s3 = potter(prices, current_item, length-(current_item+1), value + prices[current_item])
        
        return max(s1, s2, s3)


L = int(item())
prices = []
for x in range(L):
    prices.append(float(item()))

print('{:.2f}'.format(potter(prices, L-1, L-1, 0.0)))
