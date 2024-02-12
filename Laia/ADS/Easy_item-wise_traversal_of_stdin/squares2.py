import sys

def squares(n):
    M = []
    c = 0
    for _ in range(n):
        lst = []
        for _ in range(n):
            if c == 10:
                c = 0
            lst.append(str(c))
            c += 1
        M.append(lst)
    return M

a = ':('
for line in sys.stdin:
    if a != ':(':
        print()
    a = ':)'
    n = int(line.strip())
    for x in squares(n):
        print(''.join(x))