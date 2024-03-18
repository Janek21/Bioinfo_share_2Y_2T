#!/usr/bin/python3
import sys


#posar X on has passat
def treasure(x, y, i, j, map): #i, j are coordinates

    if not 0<=i<=x or not 0<=j<=y or map[i][j]=="X": #also works as:: if i not in range(x+1) or j not in range(y+1):
        return False
    
    if map[i][j]=="t":
        return True
    
    map[i][j]="X" #visited

    for next_i,next_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if treasure(x, y, i+next_i, j+next_j, map):#i+next_i, j+next_j current position + 1 to check neighbors
            return True #if a neighbor is True (treasure), return True

    return False



def main():
    firstline=sys.stdin.readline().strip("\n").split(" ")
    map_read=sys.stdin.readlines()
    starting=map_read[-1].strip("\n").split(" ")
    map_in=[]

    for line in map_read[:-1]:
        line=list(line.strip("\n"))
        map_in.append(line)

    x=int(firstline[0])-1 #size
    y=int(firstline[1])-1 #size
    i=int(starting[0])-1 #start pos
    j=int(starting[1])-1 #start pos

    if treasure(x, y, i, j, map_in):
        return "yes"
    return "no"


print(main())