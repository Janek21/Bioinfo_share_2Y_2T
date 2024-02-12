from pytokr import pytokr
item = pytokr()

def subsets(n, l, lst, sol = []):
    if n == -1:
        if len(sol) == l:
            return [sol]
        return []
    else:
        sol1 = subsets(n-1, l, lst, sol) # no l'agafa
        sol2 = []
        if len(sol2) < l:
            sol2 = subsets(n-1, l, lst, sol + [lst[n]]) # l'agafa
        return sol1 + sol2

l = int(item())
n = int(item())
lst = []
for x in range(n):
    lst.append(item())

res = subsets(n-1, l, lst)
for r in res:
    print('{', ','.join(r), '}', sep = '')