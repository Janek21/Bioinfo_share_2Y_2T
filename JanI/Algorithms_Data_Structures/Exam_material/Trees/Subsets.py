#!/usr/bin/python3
import sys

def subse(values, current_item, max_w, cand):
    if current_item==-1:
        if len(cand)<max_w:
            return [cand]
        else:
            return list()
    else:
        sol=subse(values, current_item-1, max_w, cand)
        res=subse(values, current_item-1, 
                  max_w+1, 
                  cand+[values[current_item]])
        return sol+res
    

#max_w=3
#values=["hola", "adeu", "hi"]
def main():
    max_w=int(sys.stdin.readline())
    values=sys.stdin.readline().strip("\n").split()
    sol=subse(values, len(values)-1, max_w, [])

    for x in sol:

        print("{", end="")
        print(*x, end="", sep=",")

        if x!=sol[-1]:
            print("}")
            
        else: return "}"
print(main())