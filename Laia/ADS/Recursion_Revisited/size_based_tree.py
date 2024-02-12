from pytokr import pytokr
read = pytokr()

def read_input(n):
    if n == 0:
        return tuple()
    else:
        root = int(read())
        left = int(read())
        if read == 0:
            return tuple()
        else:
            return (root, read_input(left), read_input(n-left-1))
        
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


n = int(read())
inp = read_input(n)
print("post:", *postorder(inp), '')
print("in:", *inorder(inp), '')
