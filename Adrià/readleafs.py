from pytokr import pytokr



r=pytokr()


def tree():
    x=int(r())
    if x==-1:
        return(tuple())
    return(x, tree(),tree())

c=0
def leef(t):
    global c
    if t:
        if t[1]==tuple() and t[2]==tuple():
            c+=1
        if t[1]!=tuple():
            leef(t[1])
        if t[2]!=tuple():
            leef(t[2])






tr=tree()
print(tr)
leef(tr)
print(c)








