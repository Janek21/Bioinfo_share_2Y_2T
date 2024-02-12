from pytokr import pytokr

item = pytokr()

def read_tree():
    root=int(item())
    if root==-1:
        return tuple()
    else:
        return(root, read_tree(), read_tree())

def height(tree, h):
    if tree:
        return max( height(tree[1], h+1), height(tree[2], h+1), h)
    return h-1



x = int(item())
for _ in range(x):
    tree = read_tree()
    res = height(tree, 1)

    print(res)
