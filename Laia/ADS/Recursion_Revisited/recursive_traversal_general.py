from pytokr import pytokr
read = pytokr()

children = int(read())

def reading_input():
    l = int(read()) # take from the input the node we are
    child = int(read()) # take its size
    
    children = []
    for x in range(child):
        children.append(reading_input())
    return [l, children]


def post_order(inp):    
    if not inp:     
        return []  
    res = []
    for c in inp[1]: # left
        res.extend(post_order(c)) 
    res.append(inp[0])
    return (res)
    
    
inp = reading_input()
print('', *post_order(inp))

#12
#7 3 8 0 4 2 3 1 0 1 6 0 
#5 0 2 4 9 0 1 0 8 0 5 0