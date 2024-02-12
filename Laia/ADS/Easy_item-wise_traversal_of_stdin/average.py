import sys

def average(lst):
    c = 0
    for x in lst:
        c += x
    total = c/len(lst)
    return "{:.2f}".format(total)

for x in sys.stdin:
    lst = list(map(float, x.strip().split()))
    print(average(lst))