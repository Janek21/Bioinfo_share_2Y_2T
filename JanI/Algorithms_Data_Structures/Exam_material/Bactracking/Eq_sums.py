#!/usr/bin/python3
import sys

def eq_sum(values, current_item, min_v, cand, cand_v):
    if current_item == -1:
        if cand_v == min_v:
            return [cand]
        else:
            return list()
    else: 
        "current_item >= 0" 
        sol = eq_sum(values, current_item - 1, min_v, cand, cand_v)
        res = eq_sum(values, current_item - 1, 
                min_v, 
                cand + [current_item], 
                cand_v + values[current_item])
        return sol + res


max_value=int(sys.stdin.readline().strip())
current_item=int(sys.stdin.readline().strip())
numbers=[int(x) for x in sys.stdin.readline().strip().split()]#read and place in list as integer

positions=eq_sum(numbers, current_item-1, max_value, [], 0)#list of lists of positions

for pos_ls in positions: #get lists of position
    value_ls=[]
    for individual_pos in pos_ls: #get individual positions from list of positions
        value_ls.append(int(numbers[individual_pos])) #add the values to a value list
    print("{", end="") #print opening bracket
    print(*value_ls, sep=", ", end="") #print the value list separated by commas
    print("}") #print the ending bracket
    

