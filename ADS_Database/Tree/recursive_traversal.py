from pytokr import pytokr

s = pytokr()

def read_input():
    root=int(s())
    if root==-1:
        return tuple()
    else:
        return(root, read_input(), read_input())

inp = read_input()

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

print('pos:', *postorder(inp))
print('ino:', *inorder(inp))
print(inp)
