'''
Iterative and recursive preorder traversal of trees and levelwise traversal
'''

def pre_r(tree):
    if tree:
        r = [ tree[0] ]
        r.extend(pre_r(tree[1]))
        r.extend(pre_r(tree[2]))
        return r
    else:
        return list()

def pre_i(tree):
    r = list()
    pend = list()
    pend.append(tree)
    while pend:
        t = pend.pop()
        if t:
            r.append(t[0])
            pend.append(t[2])
            pend.append(t[1])
    return r
    

from collections import deque

def levelwise(tree):
    r = list()
    pend = deque()
    pend.append(tree)
    while pend:
        t = pend.popleft()
        if t:
            r.append(t[0])
            pend.append(t[1])
            pend.append(t[2])
    return r
    

t = (3, (0, (7, (), (4, (), ())), (2, (), ())), (5, (4, (), ()), (7, (6, (), (1, (), ())), ())))

print(pre_r(t))
print(pre_i(t))
print(levelwise(t))


