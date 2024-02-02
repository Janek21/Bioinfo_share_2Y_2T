'''
This class implements the Vose algorithm: 
A Linear Algorithm For Generating Random Numbers With a Given Distribution 
@author: olao
'''

import random

class RandomMultinomial(object):
    
    '''
    Constructor
    '''
    def __init__(self, p):
        self.p = p
        self.n = len(self.p)
        self.alias = [None] * self.n
        self.prob_j = [None]* self.n
        self.build_alias()
        
    '''
    Create the alias for p
    '''
    
    def build_alias(self):
        large = []
        small = []
        for j in range(self.n):
            if self.p[j] > 1.0/self.n:
                large.append(j)
            else:
                small.append(j)
        
        
        while len(large)>0 and len(small)>0:
            j = small[0]
            k = large[0]
            large = large[1:len(large)]
            small = small[1:len(small)]
            self.prob_j[j] = self.n*self.p[j]
            self.alias[j] = k
            self.p[k] = self.p[k] + (self.p[j] - 1.0/self.n)
            
            if self.p[k] > 1.0/self.n:
                large.append(k)
            else:
                small.append(k)
        
        for l in range(len(large)):
            self.prob_j[large[l]] = 1
        for s in range(len(small)):
            self.prob_j[small[s]] = 1
    
    
    '''
    Draw a sample using the alias
    '''
                 
    def sample(self):
        j = random.randint(0,self.n-1)
        u = random.uniform(0,1)
        if(u <= self.prob_j[j]):
            return j
        return self.alias[j]
            
    
def main():    
    p = [0.1,0.2,0.2,0.5]    
    alias = RandomMultinomial(p)
    count = [0]*len(p)
    for i in range(100000):
        j = alias.sample()
        count[j] = count[j] + 1
    print(count)
    
    
if __name__ == "__main__":
    main () 
