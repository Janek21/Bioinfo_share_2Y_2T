import sys


def tree_recursive_pos():
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
        return(tree_recursive_pos(), tree_recursive_pos(), root)

out=tree_recursive_pos()
for x in str(out):
    if x.isdigit():
        print(x, end=" ")

import sys
#tornar a començar a llegir, com fer reset?
def tree_recursive_ino():
    root=sys.stdin.read(1)
    if root==" ":
        root=sys.stdin.read(1)
    if root=="-":
        next=sys.stdin.read(1)
        root=root+next
    root=int(root)
    if root==-1:
        return ""
    else:
        return(tree_recursive_ino(), root, tree_recursive_ino())
'''
out=tree_recursive_ino()
for x in str(out):
    if x.isdigit():
        print(x, end=" ")
'''