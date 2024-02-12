#!/usr/bin/python3
import sys
from pytokr import pytokr

read=pytokr()
def tree_read():
    root=str(read())
    if root=="-1":
        return tuple()
    else:
        return(root, tree_read(), tree_read())
    
def length(tree, c):
    if tree:
        return max(length(tree[1], c+1 ), length(tree[2], c+1), c)
    return c

x = int(read())
for _ in range(x):
    tree = tree_read()
    sol= length(tree, 0)

    print(sol)


'''
def length_comparison(tree, i, c):

    if i>=len(tree):
        return c #writes depth of each node
    if len(tree[i])>1:#detects if 0, () or tree with more branches ( 0, (), ())
        #fer for i in range(len(tree[i]): return length_comparison(tree[i], 0, c+1)??
        return length_comparison(tree[0], 0, c+1), length_comparison(tree[1], 0, c+1), length_comparison(tree[2], 0, c+1)#checks all subbranches of a tree/subtree with branches, adds 1 to depth
    return length_comparison(tree, i+1, c)#if the current position has no branches, goes to next one
'''