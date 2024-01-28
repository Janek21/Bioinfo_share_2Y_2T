#!/usr/bin/python3
import random


class RandomMultinomial(object):

    #Constructor
    
    def __init__(self, p): #p=array of probabilities Pa, Pc, Pt, Pg
        self.p=p #all methods can call p using self.p, p is a probability distribution
        self.n=len(self.p) #sample size (number of probabilities in the distribution)
        #store aliases and probabilities
        self.alias=[None]*self.n
        self.prob_j=[None]*self.n
        self.build_alias()#build the alias table, using following functions

    #Create alias for p
        
    def build_alias(self): #Builds the alias tables
        large=[]
        small=[]
        for j in range(self.n): #Separate probability distribution into lists (large, small) based on the number
            self.prob_j[j]=self.p[j]*self.n #calculate it now to avoid unecessary operations later
            if self.prob_j[j]>=1.0: #same as self.p[j]*self.n>1.0, but self.prob_j was caculated earlier
                #save positions of small and large probabilities (small are <1, large are >1)
                large.append(j) 
            else:
                small.append(j)
        '''
        #You could do this instead, and define self.prob_j[j] later
        if self.p[j]>1.0/self.n:
            large.append(j)
        else:
            small.append(j)
        '''
        while len(large)>0 and len(small)>0: #Create the alias tables
            last_s=small.pop() #separate last elements of the lists
            last_l=large.pop() #last_s will be the position of a probability <1, last_l will be the position of a probability >1

            self.alias[last_s]=last_l #Assign an alias
            self.prob_j[last_l]=self.prob_j[last_l]+self.prob_j[last_s]-1 #update the probability lists

            if self.prob_j[last_l]<1.0: #Using updated probability list reorganize probability distribution
                small.append(last_l) 
            else:
                large.append(last_l)
    
    def sample(self):
        #determine column to inspect
        p_i=random.choice(self.prob_j)  #Choose a random probability among our list
        p_i_Position=self.prob_j.index(p_i) #We define the position of the randomly chosen probability as a variable using index, this is to avoid unnecessary repetition
        if p_i>random.uniform(0,1): #compare column with random sample to determine if we use a probability or its alias
            return p_i_Position
        else:
            return self.alias[p_i_Position]     


def main():
    p=[0.1,0.2,0.2,0.5] #expected #0.1, 0.4, 0.3, 0.2
    alias=RandomMultinomial(p)#create alias as a type of RandomMultinomial, i can do all things specified in the class
    count=[0]*len(p)#create len(p) spaces in list
    #test if numbers in p are accurate(expected result) -> create an observation over 10000 elements
    for _ in range(10000):
        j=alias.sample()#sample is function of class, j is a number
        #j is random number used as position --> add 0.0001 to a random position(position j, which is an index in range of our list) --> repeat until total ==1(10000 times later)--> array of random numbers
        count[j]=count[j]+1.0/10000.0 
    print(count) #count is a vector, very similar to p, count is observed


if __name__=="__main__":
    main()