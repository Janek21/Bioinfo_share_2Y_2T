#!/usr/bin/python3

import sys

def trace(best, goal):
    coins = []
    while goal:
        if len(best)<=goal:
            return -1
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



text=sys.stdin.readlines()

for line in text:
    line=line.strip("\n").split(" ")
    goal=int(line[0])
    denoms=[int(x) for x in line[3:]]

    ls =min_change(goal, denoms)
    print(ls)
    tr=trace(ls, goal)
    if tr==-1:
        print("no")
    elif tr:
        print(tr)
        print(len(tr))
    else:
        print(0)



'''
def trace(best, goal):
    if best==[-1]:
        return 0
    coins = []
    while goal:
        if len(best)<=goal:
            return "no"
        use = best[goal]
        coins.append(use)
        goal -= use
    return len(coins)
'''