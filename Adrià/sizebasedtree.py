from pytokr import pytokr

r=pytokr()

def tree(t):
    if t<0:
        return(tuple())

    x=r()
    n=int(r())
    return(x,tree(n-1),tree(t-int(n)-1))

def pos(t):
    if t:
        pos(t[1])
        pos(t[2])
        print(t[0], end=' ')
    return

def ins(t):
    if t:
        ins(t[1])
        print(t[0],end=' ')
        ins(t[2])
    return

t=r()

tree=tree(int(t)-1)
print('post:',end=' ')
pos(tree)
print()
print('in:',end=' ')
ins(tree)


