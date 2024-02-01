#!/usr/bin/python3
import sys

def min_change(values, current_item, max_v, max_w, comb, comb_v, comb_w):
    #if current_item==-1:
    if comb_v==max_v and comb_w<=max_w:
        return [comb]
    elif comb_v>max_v or comb_w==max_w:
        return list()
    else:
        comb_list=[]
        '''
        sol=min_change(values, current_item-1, max_v, max_w, 
                        comb+[values[current_item]], 
                        comb_v+values[current_item], 
                        comb_w+1)
        res=min_change(values, current_item-1, max_v, max_w,
                       comb)
        '''
        sol=min_change(values, current_item - 1, max_v, max_w,comb, comb_v, comb_w)
        res=min_change(values, current_item-1, max_v, max_w,
                       comb+values[current_item],
                       comb_v+values[current_item],
                       comb_w+1)
        return sol+res


def main():
    if c < min(values):
        return 0
    
    result = min_change(values, len(values)-1, c, n, [], 0, 0)
    if len(result)>0: #no sum of values can give c
        result = str(result)
        result = result.replace("], [", "-").replace("[", "").replace("]", "")
        result = result.split("-")
        
        result=[result[position].split(", ") for position in range(len(result))]
        print(result)
        return len(min(result))
    
    else:
        return "no"


#[[[[[6, 6, 6, 2]], [[6, 6, 4, 4]]]]]
text=sys.stdin.readlines()
for line in text:

    line=line.strip("\n").split(" ")
    c=int(line[0])
    n=int(line[1])
    values=[int(x) for x in line[3:]]
    print(min_change(values, len(values)-1, c, n, [], 0, 0))
