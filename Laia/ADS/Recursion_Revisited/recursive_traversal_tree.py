from pytokr import pytokr
read = pytokr()

def read_input(size):
    if size == 0:
        return tuple()
    else:
        root = int(read())
        if root == -1:
            return tuple()
        else:
            return (root, read_input(size-1), read_input(size-1))
    
def postorder(tree):
    if not tree:
        return []
    else:
        root = [tree[0]]
        left = postorder(tree[1])
        right = postorder(tree[2])
        return left + right + root

def inorder(tree):
    if not tree:
        return []
    else:
        root = [tree[0]]
        left = inorder(tree[1])
        right = inorder(tree[2])
        return left + root + right

size = int(read())
inp = read_input(size)

p = postorder(inp)
i = inorder(inp)
print('',*p)
print('',*i)


