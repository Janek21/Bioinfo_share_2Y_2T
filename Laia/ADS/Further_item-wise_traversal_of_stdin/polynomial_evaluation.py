import sys

def poly(x, a):
    result = 0
    for i in range(len(a)):
        num = a[len(a)-i-1]
        result += num*(x**i)
    return '{:.4f}'.format(result)

x = float(sys.stdin.readline().strip())
a = list(map(float, sys.stdin.readline().strip().split()))
print(poly(x, a))