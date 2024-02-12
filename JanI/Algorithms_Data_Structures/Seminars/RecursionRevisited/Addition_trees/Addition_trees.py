#!/usr/bin/python3

import sys

from pytokr import pytokr

read=pytokr()
def tree_recursive_py():
    root=read()
    if root!="+":
        root=(float(root)* 10000)/10000
        return float(root)
    else:
        return [root, tree_recursive_py(), tree_recursive_py()]

#+ + 5 + 2 3 90
#['+', ['+', 5.0, ['+', 2.0, 3.0]], 90.0]

def evaluator(tree):
    if type(tree)==float:
        return tree

    tree[0]=evaluator(tree[1])+evaluator(tree[2])
    return tree[0]
'''
def preorder(tree):
    ls=[]
    t=0
    for x in tree:
        if type(x)!=list:
            ls.append(x)
        else:
            t=1
            ls.extend(x)
    if t==1:
        return preorder(ls)
    return ls
'''

def preorder(tree):
    if type(tree)==float:
        return [tree]
    elif type(tree)==list:
        ls=[]
        for x in tree:
            ls+=preorder(x)

        return ls
    else:
        return []

def postorder(tree):
    if type(tree)==float:
        return [tree]
    left=postorder(tree[1])
    right=postorder(tree[2])
    return left+right+[tree[0]]

def inorder(tree):
    if type(tree)==float:
        return [tree]
    left=inorder(tree[1])
    right=inorder(tree[2])
    return left+[tree[0]]+right


tree=tree_recursive_py()
evaluator(tree)

ls_pre = preorder(tree)
ls_ino = inorder(tree)
ls_post = postorder(tree)
pre=[]
ino=[]
post=[]

for p in ls_pre:
    pre.append('{:.4f}'.format(p))

for p in ls_ino:
    ino.append('{:.4f}'.format(p))

for p in ls_post:
    post.append('{:.4f}'.format(p))

print(*pre, end=" \n")
print(*ino, end=" \n")
print(*post, end=" \n")

