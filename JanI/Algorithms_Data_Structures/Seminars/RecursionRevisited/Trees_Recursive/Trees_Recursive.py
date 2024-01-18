import sys
from pytokr import pytokr
''' NOT WORK IN JUTGE FOR PRIVATE CASES, poser problemes en numeros de 2 digits
def tree_read():
    root=sys.stdin.read(1)
    if root==" ":
        root=sys.stdin.read(1)
    next=sys.stdin.read(1)
    if root=="-":
        root=root+next
    if next!=" ":
        root=root+next
    root=int(root)
    if root==-1:
        return tuple()
    else:
        return(root, tree_read(), tree_read())
'''
def reader(num):
    c_num=sys.stdin.read(1)
    if c_num!=" ":
        if len(num)!=0:
            num=num[0] + c_num,
        else:
            num=tuple(c_num)
        return reader(num)
    root=int(''.join(num))
    if root==-1:
        return tuple()
    else:
        return(root, reader(tuple()), reader(tuple()))


read=pytokr()
def tree_read():
    root=int(read())
    if root==-1:
        return tuple()
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
print("pos:", *pos)
print("ino:", *ino)
