#!/usr/bin/python3
import sys

from pytokr import pytokr
item, items = pytokr(iter = True)


def treesearch(element, treezone):
    if not treezone:
        return False
    if treezone[0]==element:
        return True
    if treezone[0] > element:
        return treesearch(element, treezone[1])
    if treezone[0]<element:
        return treesearch(element, treezone[2])
    return False

def tree_recursive_py():
    root=int(item())
    if root==-1:
        return tuple()
    else:
        return(root, tree_recursive_py(), tree_recursive_py())

number = int(item())
tree =  tree_recursive_py()

for number in items():
    n = int(number)
    res = (treesearch(n, tree))
    if res:
        print(n, end = "")
        print(' ', end = "")
        print(1)
    else:
        print(n, end = "")
        print(' ', end = "")
        print(0)

#la sucia
'''
dscard=sys.stdin.readline()
t=sys.stdin.readline().strip().split()
tofind=sys.stdin.readlines()
for x in tofind:
    x=x.strip()
    if x in t:
        print(x, 1)
    else:
        print(x, 0)
    

'''