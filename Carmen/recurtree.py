from pytokr import pytokr

s=pytokr()
size = int(s())

'''
the input is almost identical to the first recursive tree function THIS TIME we have a size we need to ignore: 
it goes like size /n and then the tree
'''

def reading_input():    #DEFINE THE TREE    
    l=int(s())      # make the inout number an integer
    if l==-1:   #check if it's a leaf
        return tuple()  #if it is  then return an emoty tuple because after this there are no more children     
    else:   #otherwise we have a "root"
        return (l, reading_input(), reading_input())    # Recursively build the left and right subtrees by calling 'reading_input' again
    
inp=reading_input()     #call the reading input to define the tree

def post_order(inp):    #our first order of business
    if not inp:     #if there is no more inout or it is empty
        return []   # return an empty list
    else:   #if thre is  input
        left=post_order(inp[1]) #assign the left node as the first one right after our current node since we are working with binary trees 
        right=post_order(inp[2])    #assign the right tree as the secode node after the one we are currently on 
        return left+ right + [inp[0]]       # return the order of first the left child, then the right and then the root so the node we currently on
    
    
def inorder(inp):       #for inorder, second order of business
    if not inp: #if the input is empty  
        return []   #return an empty list
    else:   #otherwise
        left= inorder(inp[1])   #assign as always the left child as the first one right after our current node
        right= inorder(inp[2])  #assign the right one as the one after the left one 
        return left+ [inp[0]] + right   #return the left child first, then the root and then the right child
    
    
    
print('', *post_order(inp)) #print our tree according to postorder  
print('', *inorder(inp))    #print our tree according to inorder 
