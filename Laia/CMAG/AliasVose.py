import random

class RandomMultinomial(object):
    '''
    Constructor
    '''
    def __init__(self, p):
        # initialization of the variables for being able to use them in the functions
        self.p = p # define p
        self.n = len(self.p) # define n as the number of elements in p
        self.alias = [None]*self.n # there are as many alias as elements in p
        self.prob_j = [None]*self.n # it contains as many elements as p
        self.build_alias() # call the function to define the alias

    '''
    Create the alias for p
    '''
    def build_alias(self):
        # initialize 2 empty lists for small and large values
        large = [] # here will go probabilities larger than 1/n
        small = [] # here will go probabilities smaller than 1/n

        # fill the lists depending if the values are smaller or larger than 1/n
        for j in range(self.n): # iterate over the length of p
            if self.p[j] >= 1.0/self.n:
                large.append(j) # add probabilities larger than 1/n
            else:
                small.append(j) # add probabilities smaller than 1/n
            
        while len(small) != 0 and len(large) != 0:
            # get the last item of the list and delete it from the list
            j = small.pop() # j is the last item of small
            k = large.pop() # k is the last item of large

            self.alias[j] = k # the alias of j is k
            self.p[k] += self.p[j] - 1.0/self.n # get each probability of k (large)

            # prob_j of each j is n multiplied by the probability of j (associated probability)
            self.prob_j[j] = self.n * self.p[j] 

            # change the probabilities to the list they belong to (as in line 25)
            if self.p[k] >= 1.0/self.n:
                large.append(k)
            else:
                small.append(k)
            
        # remaining elements must be 1 (they may not be 1 due to rounding errors)
        while len(small) > 0:
            self.prob_j[small.pop()] = 1.0
            
        while len(large) > 0:
            self.prob_j[large.pop()] = 1.0

    '''
    Create the sample function
    '''
    def sample(self):
        i = random.randint(0, self.n-1) # get a random value between 0 and n-1 --> [0, n)
        u = random.uniform(0, 1) # get a random value between 0 and 1
        if self.prob_j[i] >= u: # u is smaller or equal to the associated probability of i
            return i # return i as it is in the associated probability
        return self.alias[i] # otherwise return the alias

def main():
    p = [0.1, 0.2, 0.2, 0.5]
    alias = RandomMultinomial(p) # the alias will have all the functions of the RandomMultinomial class (alias = RandomMultinomial object)
    count = [0]*len(p) # count has as many elements as p (where the result will be stored)
    for _ in range(100000): # iterate over 100000
        j = alias.sample() # get a random sample
        count[j] += 1.0/100000.0 # add 1 over the total number of samples (as the sample has alredy come out)
    print(count) 

if __name__ == "__main__":
    main()