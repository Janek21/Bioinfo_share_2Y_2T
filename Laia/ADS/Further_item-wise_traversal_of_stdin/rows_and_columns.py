import sys

def row(M, r):
    lst = []
    for i in range(len(M[0])):
        lst.append(M[r-1][i])
    return lst

def col(M, c):
    lst = []
    for i in range(len(M)):
        lst.append(M[i][c-1])
    return lst

s = sys.stdin.readline().strip().split()
m = int(s[0])
n = int(s[1])
M = [[ele for ele in sys.stdin.readline().strip().split()] for _ in range(m)]
z = sys.stdin.readline().strip().split()

for line in sys.stdin:
    line = line.strip().split()
    if line[0] == 'row':
        print('row ', line[1], ': ', ' '.join(row(M, int(line[1]))), sep = '')
    elif line[0] == 'column':
        print('column ', line[1], ': ', ' '.join(col(M, int(line[1]))), sep = '')
    else: #element
        r = int(line[1])-1
        c = int(line[2])-1
        print('element ', line[1], ' ', line[2], ': ', M[r][c], sep = '')
