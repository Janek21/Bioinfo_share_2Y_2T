from pytokr import pytokr

s=pytokr()
def reading_input(size):
    if size == 0:
        return tuple()
    l=int(s())
    sizeleft=int(s())
    return (l, reading_input(sizeleft), reading_input(size-1-sizeleft))

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

size = int(s())
inp=reading_input(size)
#print(inp)
print('post:', *postorder(inp))
print('in:', *inorder(inp))

