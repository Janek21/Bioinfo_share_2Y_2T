import sys

def squares(n):
    M = [[str(n) for _ in range(n)] for _ in range(n)]
    return M

a = ':('
for line in sys.stdin:
    if a != ':(':
        print()
    a = ':)'
    n = int(line.strip())
    for x in squares(n):
        print(''.join(x))