#!/usr/bin/python3
import sys

def eq_sum(values, current_item, min_v, cand, cand_v, ls):
    if current_item == -1:
        if cand_v == min_v:
            return [cand]
        else:
            return list()
    else: 
        "current_item >= 0" 
        sol = eq_sum(values, current_item - 1, min_v, cand, cand_v, ls)
        res = eq_sum(values, current_item - 1, 
                min_v, 
                cand + [current_item], 
                cand_v + values[current_item], ls)
        ls.append(res)



def main():
    max_value=int(sys.stdin.readline().strip())
    current_item=int(sys.stdin.readline().strip())
    numbers=[int(x) for x in sys.stdin.readline().strip().split()]#read and place in list as integer

    ls=[]
    eq_sum(numbers, current_item-1, max_value, [], 0, ls)#list of lists of positions

    for pos_ls in ls: #get lists of position
        if pos_ls:
            return pos_ls

print(main())

