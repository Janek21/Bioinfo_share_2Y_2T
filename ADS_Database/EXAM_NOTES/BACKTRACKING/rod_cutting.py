from pytokr import pytokr

def rod_cutting(list, pos, cands, candw, candv, maxw):
    if candw > maxw:
        return float('-inf')
    if pos == -1:
        if candw <= maxw:
            return candv
        else:
            return float('-inf')
    else:
        option1 = rod_cutting(list, pos-1, cands, candw, candv, maxw)
        option2 = rod_cutting(list, pos-1, cands + [pos+1], candw+pos+1, candv + list[pos], maxw)
        option3 = rod_cutting(list, pos,  cands + [pos+1], candw+pos+1, candv + list[pos], maxw)
        
        return max(option1, option2, option3)
    
item = pytokr()
reps = int(item())
price = []
for x in range(reps):
    price.append(float(item()))
res = rod_cutting(price, len(price)-1, [], 0, 0, reps)
print('{:.2f}'.format(res))
        