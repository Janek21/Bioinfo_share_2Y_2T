import sys

def find(i, j, map, x, y):    
    if i not in range(x+1) or j not in range(y+1):
        return False
    if map[i][j] == 'X':
        return False
    if map[i][j] == 't':
        return True
    
    map[i][j] = 'X'
    up = find(i-1, j, map, x, y)
    if up: 
        return True
    down = find(i+1, j, map, x, y)
    if down: 
        return True
    right = find(i, j+1, map, x, y)
    if right: 
        return True
    left = find(i, j-1, map, x, y)
    if left: 
        return True
    return False


t = sys.stdin.readlines()

(x, y)= tuple(t[0].strip().split())
(i, j) = tuple(t[-1].strip().split())
map = [list(line[:-1]) for line in t[1:-1]]

print('yes' if find(int(i)-1,int(j)-1,map,int(x)-1,int(y)-1) else 'no')

