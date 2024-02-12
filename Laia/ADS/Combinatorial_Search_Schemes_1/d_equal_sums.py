from pytokr import pytokr
item, items = pytokr(iter = True)

def equal_sums(num, s, n):
    M = [[0 for _ in range(s+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, s+1):
            if num[i-1] <= j:
                M[i][j] = M









s = int(item())
n = int(item())
num = []
for x in range(n):
    num.append(int(item()))

res = equal_sums(num, s, n)
for x in res:
    print('{', ','.join(map(str,x)), '}', sep = '')