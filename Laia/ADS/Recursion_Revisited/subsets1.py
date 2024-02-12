from pytokr import pytokr
item = pytokr()

def subsets(n, lst, sol = []):
    if n == -1:
        return [sol]
    else:
        sol1 = subsets(n-1, lst, sol) # no l'agafa
        sol2 = subsets(n-1, lst, sol + [lst[n]]) # l'agafa
        return sol1 + sol2

n = int(item())
lst = []
for x in range(n):
    lst.append(item())

res = subsets(n-1, lst)
for r in res:
    print('{', ','.join(r), '}', sep = '')