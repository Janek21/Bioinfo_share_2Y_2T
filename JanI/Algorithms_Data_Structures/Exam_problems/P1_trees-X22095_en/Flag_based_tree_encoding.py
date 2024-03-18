#!/usr/bin/python3

from pytokr import pytokr

#3 1 1 0 1 1 7 -1 1 4 -1 -1 2 -1 -1 5 1 1 4 -1 -1 7 1 -1 6 -1 1 1 -1 -1
#(3, (0, (7, (), (4, (), ())), (2, (), ())), (5, (4, (), ()), (7, (6, (), (1, (), ())), ())))

read=pytokr()
def tree_read():
    root=int(read())
    left=int(read())
    right=int(read())
    if left==-1 and right==-1:
        return (root, tuple(), tuple())
    if right==-1:
        return (root, tree_read(), tuple())
    if left ==-1:
        return (root, tuple(), tree_read())
    else:
        return(root, tree_read(), tree_read())

def tree_recursive_pos(numlist):
    if not numlist:
        return []
    left=tree_recursive_pos(numlist[1])
    right=tree_recursive_pos(numlist[2])
    return left+right+[numlist[0]]

def tree_recursive_ino(numlist):
    if not numlist:
        return []
    left=tree_recursive_ino(numlist[1])
    right=tree_recursive_ino(numlist[2])
    return left+[numlist[0]]+right


numlist=tree_read()
pos=tree_recursive_pos(numlist)
ino=tree_recursive_ino(numlist)
print("post:", *pos, end=" \n")
print("in:", *ino, end=" \n")