from pytokr import pytokr
read = pytokr()

def read_input():
    root = int(read())
    if root == -1:
        return tuple()
    else:
        return(root, read_input(), read_input())

def postorder(tree): #left --> right --> root
    if not tree:
        return []
    else:
        root = [tree[0]]
        left = postorder(tree[1])
        right = postorder(tree[2])
        return left + right + root

def inorder(tree): #left --> root --> right
    if not tree:
        return []
    else:
        root = [tree[0]]
        left = inorder(tree[1])
        right = inorder(tree[2])
        return left + root + right
    
inp = read_input()
print(inp)
print("pos:", *postorder(inp))
print("ino:", *inorder(inp))

