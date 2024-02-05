from pytokr import pytokr
s=pytokr()
def reading_input(size):
    if size == 0:
        return tuple()
    l=int(s())
    sizeleft=int(s())
    if s == 0:
        return tuple() 
    else:
        return (l, reading_input(sizeleft), reading_input(size-1-sizeleft))
    
def post_order(inp):
    if not inp:
        return []
    else:
        left=post_order(inp[1])
        right=post_order(inp[2])
        return left+ right + [inp[0]]
        
        
def inorder(inp):
    if not inp:
        return []
    else:
        left= inorder(inp[1])
        right= inorder(inp[2])
        return left+ [inp[0]] + right
        

size = int(s())
inp=reading_input(size)
#print(inp)
print('post:', *post_order(inp), '')
print('in:', *inorder(inp), '')
