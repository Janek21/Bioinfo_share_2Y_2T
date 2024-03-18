from pytokr import pytokr
read = pytokr()

def read_input():
    root = int(read())
    left = int(read())
    right = int(read())
    if left == -1 and right == 1:
        return (root, tuple(), read_input())
    elif left == 1 and right == -1:
        return (root, read_input(), tuple())
    elif left == 1 and right == 1:
        return (root, read_input(), read_input())
    else:
        return (root, tuple(), tuple())

def postorder(inp):
    if not inp:
        return []
    else:
        left = postorder(inp[1])
        right = postorder(inp[2])
        return left + right + [inp[0]]
def inorder(inp):
    if not inp:
        return []
    else:
        left = inorder(inp[1])
        right = inorder(inp[2])
        return left + [inp[0]] + right

inp = read_input()

print('post:', *postorder(inp))
print('in:', *inorder(inp))
