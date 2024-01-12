import sys
def tree_read():
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