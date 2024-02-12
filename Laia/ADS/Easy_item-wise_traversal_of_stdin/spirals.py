import sys

def spirals(n):
    M = [['.' for _ in range(n)] for _ in range(n)]
    return spirals_aux(M, 0, n-1)

def spirals_aux(M, start, end):
    if start > end:
        return M
    else:
        for i in range(start, end+1):
            M[end][i] = 'X' #abaix
            M[i][end] = 'X' #dreta
        
        for i in range(start+1, end):
            M[start][i] = 'X' #adalt
        
        for i in range(start, end-1):
            M[i][start+1] = 'X' #esquerra

        return spirals_aux(M, start+2, end-2)
        

for line in sys.stdin:
    line = int(line.strip())
    if line != 0:
        for x in spirals(line):
            print(''.join(x))
        print()