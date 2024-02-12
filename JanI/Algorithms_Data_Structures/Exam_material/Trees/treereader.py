import sys

def tree_recursive():
    root=sys.stdin.read(1)
    if root==" ":
        root=sys.stdin.read(1)
    if root=="-":
        next=sys.stdin.read(1)
        root=root+next
    root=int(root)
    if root==-1:
        return tuple()
    else:
        return(root, tree_recursive(), tree_recursive())
print(tree_recursive())
#################################### More recursive
import sys

def tree_recursive():
    root=sys.stdin.read(1)
    if root=="-":
        next=sys.stdin.read(1)
        root=root+next
    if root!=" ":
        root=int(root)
        if root==-1:
            return tuple()
        else:
            return(root, tree_recursive(), tree_recursive())
    else:
        return(tree_recursive())
print(tree_recursive())
##################################### Pytokr
from pytokr import pytokr

read=pytokr()
def tree_recursive_py():
    root=int(read())
    if root==-1:
        return tuple()
    else:
        return(root, tree_recursive_py(), tree_recursive_py())
print(tree_recursive_py())

