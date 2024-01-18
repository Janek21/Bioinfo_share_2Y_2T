#!/usr/bin/python3
import random


class RandomMultinomial(object):

    #Constructor
    
    def __init__(self, p): #p=array of probabilities Pa, Pc, Pt, Pg
        self.p=p#tothom(all methods) pot cridar p amb self.p
        self.n=len(self.p)
        self.alias=[None]*self.n
        self.prob_j=[None]*self.n
        self.build_alias()#build all these variables, using next function

    #Create alias for p
        
    def build_alias(self):
        large=[]
        small=[]
        for j in range(self.n):
            if self.p[j]>1.0/self.n:#same as self.p[j]*self.n>1.0
                large.append(j)#save positions of small and large probabilities
            else:
                small.append(j)
        while len(small)>0 and len(large)>0:
            
    
    def sample():
        #determina column to inspect
        p_i=random.choice(self.prob_j)
        #determine
        if prob_j[p_i]>=random.uniform(0,1):
            return p_i
    
        


def main():
    p=[] #expected #0.1, 0.4, 0.3, 0.2
    alias=RandomMultinomial(p)#create alias as a type of RandomMultinomial, i can do all thins specified in class
    count=[0]*len(p)#create len(p) spaces in list
    #test if numbers in p are accurate(expected result) -> create an observation over 10000 elements
    for _ in range(10000): #can use i
        j=alias.sample()#sample is function of class #j is a number
        count[j]=count[j]+1.0/10000.0 
    print(count) #count is a vector, very similar to p, count is observed


if __name__=="__main__":
    main()


def random_seq():
    print(random.randrange(0,100))
    return random.uniform(0,1)
print(random_seq())

def seq_prob():
    P_list=input("Input the probabilities of the elements separated by a space").split()
    '''
    pa=input("Input the probability of A")
    pc=input("Input the probability of C")
    pt=input("Input the probability of T")
    pg=input("Input the probability of G")
    P_list=[pa, pc, pt, pg]
    '''
    return P_list

print(seq_prob())