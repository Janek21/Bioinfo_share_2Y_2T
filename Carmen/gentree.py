from pytokr import pytokr

s= pytokr()
children= int(s())

'''
THIS IS NOT A BINARY TREE!!!!!
FIRST NB IS THE NB OF NODES TOTAL. THEN SECOND NODE IS OUR ROOT, RIGHT AFTER IS THE NB OR CHILDREN. AND THEN WE START FROM THE LEFT THE CHILDREN AND KEEP MOVING ACROSS THE TREE 
'''

def reading_input():        #define the tree according to the size we get
    l=int(s())  #take from the input the node we are on as integer
    child=int(s())   #take its size as int 
    children=[]
    for x in range(child):
        children.append(reading_input())
    return [l, children]


def post_order(inp):    
    if not inp:     
        return []  
    res=[]
    for c in inp[1]:
        res.extend(post_order(c))
    res.append(inp[0])
    return (res)
    
    
inp=reading_input()
print(inp)
print('', *post_order(inp))


