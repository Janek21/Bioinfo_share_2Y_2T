#!/usr/bin/python3
import sys

def trace(best, goal):
    coins = []
    while goal:
        use = best[goal]
        coins.append(use)
        goal -= use
    return coins


def min_change(goal, denoms):
    denoms = [0] + list(denoms) #denoms = 0, ...
    table = [ float("inf") ] * (goal + 1)
    table[0]=0
    best=[-1]* (goal+1)
    for coin_pos in range(1,len(denoms)): #coin2 has pos1, ...
        for x in range(denoms[coin_pos], goal+1): #x=2=denoms[1]
            
            #table[x]=min(1 + table[x - denoms[coin_pos]], table[x])
            if 1 + table[x - denoms[coin_pos]]<table[x]:
                table[x]=1+table[x-denoms[coin_pos]]
                best[x]=denoms[coin_pos]
    return best
    #return table[goal], best

def main():
    text=sys.stdin.readlines()

    for line in text:
        line=line.strip("\n").split(" ")
        goal=int(line[0])
        denoms=[int(x) for x in line[3:]]
    #goal = 20
    #denoms =[2, 4, 6, 17]
        ls =min_change(goal, denoms)
        tr=trace(ls, goal)
        if tr:
            print(tr)
        else:
            print(0)

print(main())