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

def length_comparison(tree, i, c):
    '''in repeated action in multiple loops -> recursion
    c=0
    for subtree in tree[i]:
        if len(subtree)>1:
            c+=1
            for x in subtree:
                if len(x)>1:
                    c+1
                    #...
    '''
    if i>=len(tree):
        return c #writes depth of each node
    if len(tree[i])>1:#detects if 0, () or tree with more branches ( 0, (), ())
        #fer for i in range(len(tree[i]): return length_comparison(tree[i], 0, c+1)??
        return length_comparison(tree[0], 0, c+1), length_comparison(tree[1], 0, c+1), length_comparison(tree[2], 0, c+1)#checks all subbranches of a tree/subtree with branches, adds 1 to depth
    return length_comparison(tree, i+1, c)#if the current position has no branches, goes to next one

treenum=read()
for _ in range(int(treenum)):
    tree=tree_read()
    node_depth=length_comparison(tree, 0, 1)
    m=0
    for node in str(node_depth):#iterate through the tuple as a string
        if node.isdigit():#discard all non-digits
            node=int(node)
            if node>m:#get maximum of all numbers, if node > m, subsitute m
                m=node
    print(m)

