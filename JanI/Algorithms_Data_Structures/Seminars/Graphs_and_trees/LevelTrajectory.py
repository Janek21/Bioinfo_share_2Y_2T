#!/usr/bin/python3
import sys
from pytokr import pytokr

read=pytokr()
def tree_read():
    root=int(read())
    if root==-1:
        return list()
    else:
        return[root, tree_read(), tree_read()]

def tree_leveling(numlist):
    if not numlist:
        return []
    print(numlist[0])
    left=tree_leveling(numlist[1])
    right=tree_leveling(numlist[2])
    
    #return 

def print_levels(lst, out, level=1):
    if not lst:
        return
    for item in lst:
        if isinstance(item, list):
            print_levels(item, out, level + 1)
        else:
            #print(f"level {level}: {item}") #prints level 1 x, level 2 x, level 3 x, level 2 x, change that to group levels together

            if len(out)>=level: #if we have that level (position)

                out[level-1]=out[level-1]+[item]

            elif len(out)<level: #if we dont have that level yet (level is larger than our length) we create a new level

                out.append([item])
    return out

def main():
    useless=int(read())
    numlist=tree_read()
    
    sol= print_levels(numlist, []) #get elemet 1 for level 1 get element 1 from list 2 for level 2, etc

    for lvl in range(len(sol)):
        print(f"level {lvl+1}: ", end="")
        print(*sol[lvl])

if __name__ == "__main__":
    main ()

