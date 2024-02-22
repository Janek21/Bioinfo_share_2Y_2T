#!/usr/bin/python3

#class
#function named union that creates tree from a to b
#if a +b(tree), b is added to the root of a (if it has any) from its root

#store for each node its parent, if its root, point to itself 

class ourUnionFind(object): #input is dictionary as a value list, the key is a number and its value is the same num initially (change to root)

    def __init__(self, indict):
        self.indict=indict
    
    def new(self, x): #x is insertion to tree(dict)
        self.indict[x]=x #define 
    
    def find(self, v): #find v in tree, this is path comprehension VV

        if v==self.indict[v]: #check if the key and value of our number is the same (if its a root)
            return self.indict[v] #if it is a root, return it
        
        self.indict=self.find(self.indict[v]) #if its not a root look at its values (children)
        return self.indict[v] ##return the value at the bottom

    def union(self, x, y): #add values of x and y, root of y is tottal root

        add=self.find(x) #search for the root of x
        base=self.find(y)#search for the root of y
        
        if base!=add: #if they are in different trees
            self.indict[base]=add #add the tree containing x (rood is add) into root base
            #not append in case its a tree and not a single number

def main():
    #d={1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7} #WRONG DICT
    d={}
    uf=ourUnionFind({}) #provar treure object and __init__
    for x in range(10):
        uf.new(x)
    uf.union(2, 3)
    uf.union(6,7)
    uf.union(7,8)
    uf.union(2,7)
    uf.find(2)
    print(uf.indict)
print(main())

class OurGraph(object):

    def __init__(self, indict):
        self.indict=indict

    def add_edge(self, u, v, w):
        self.indict[u][v]=w

    def edges(self):
        for u in self.indict.keys():
            for v in self.indict.values():
                print(self.indict[u][v])