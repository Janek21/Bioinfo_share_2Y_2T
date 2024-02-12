from pytokr import pytokr
item, items = pytokr(iter = True)

def equal_sums(num, s, current_item, cand = []):
    if current_item == -1:
        if s == 0:
            return [cand]
        return []
    else:
        s1 = equal_sums(num, s, current_item-1, cand)
        s2 = equal_sums(num, s-num[current_item], current_item-1, cand+[num[current_item]])
        return s1 + s2

s = int(item())
n = int(item())
num = []
for x in range(n):
    num.append(int(item()))

res = equal_sums(num, s, n-1)
for x in res:
    print('{', ','.join(map(str,x)), '}', sep = '')