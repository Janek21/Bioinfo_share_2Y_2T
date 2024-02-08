#!/usr/bin/python3

import sys

#canvi de functionament: max_v es el maxim que tinc en aquell moment, per identificar la millor combinacio
def rod_cut(table, current_item, max_v, max_w, cand, cand_v, cand_w):
    if cand_w==max_w:
        return cand
    elif cand_w>max_w:
        return list()
    else:
        value_list=[]
        for i in range(current_item, -1, -1):
            new_comb=cand+[table[i]]
            sol=rod_cut(table, i, max_v, max_w,
                        new_comb,
                        cand_v+table[i],
                        cand_w+(i+1))
            if type(sol)==list and sum(sol)>max_v:
                max_v=sum(sol)
                value_list.append(sum(sol))
        return value_list
    
#max_w=5
#table=[1.0, 2.4, 3.0, 4.0, 4.5]
#print((rod_cut(table, len(table)-1, 0.0, max_w, [], 0, 0))) #add max

def main():
    rod=sys.stdin.readline()
    text=sys.stdin.readlines()
    table=[]
    for line in text:

        line=line.strip("\n").split()
        line=[float(x) for x in line]
        table=table+line

    return max(rod_cut(table, len(table)-1, 0.0, float(rod), [], 0, 0))
print(main())
