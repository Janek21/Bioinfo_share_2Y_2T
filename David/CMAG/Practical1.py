import random

class RandomMultinomial(object):             #define a class that will contain the necessary functions __init__(), build.alias() and sample()
    '''
    Constructor
    '''
    def __init__(self, p):                   #this funcion is a constructor function that gives us the values to use in the next funcions
        self.p = p                           #define the self.p variable as the p we give as input, that is the probabilities list
        self.n = len(self.p)                 #define the self.n variable to be the length of the list p
        self.alias = [None] * self.n         #define self.alias to be an empty list with length of self.n and every item being 'None'
        self.prob_j = [None] * self.n        #define self.prob_j to be n empty list with length of self.n and every item being 'None'
        self.build_alias()                   #execute the function build alias that recieves as inputs the previus variables and is defined next

    def build_alias(self):                   #this function will build the alias using as input the variables defined in the __init__ function
        large = []                           #define an empty list called large in which we will append a value if its bigger than the threshold 1/num of probabilities
        small = []                           #define an empty list called small in which we will append a value if its smaller than the threshold 1/num of probabilities
        l = len(large)                       #define as l the length of the list large, initially it will be 0
        s = len(small)                       #define as s the length of the list small, initially it will be 0
        for j in range(self.n):              #initialize a for loop that will use j as a variable that will take every value of the range of self.n every loop
            if self.p[j] >= 1.0/self.n:      #check if for every position of the list of probabilities are bigger than the threshold (with 4 probabilities the threshold would be 0.25)
                large.append(j)              #the item is bigger, so we append it to the large list
                l += 1                       #the item is bigger, so we sum 1 to the counter of the length of large because we added 1 item and thus the length increased
            else:                            #if the item in a given position is smaller then the threshold, it enters in this condition
                small.append(j)              #the item is smaller, so we append it to the small list
                s += 1                       #the item is smaller, so we sum 1 to the counter of the length of small because we added 1 item and thus the length increased
        while s != 0 and l != 0:             #initialize a while loop that will run until both lists, large and small, are empty, or in other words, until its lengths, l and s, are 0
            s -= 1                           #substract one to the counter of the length of small so in the next loop it picks another item of the list
            j = small[s]                     #let the variable j be the item of the list small in the position s
            l -= 1                           #substract one to the counter of the length of large so in the next loop it picks another item of the list
            k = large[l]                     #let the variable k be the item of the list large in the position l
            self.prob_j[j] = self.n * self.p[j]                     #append to the list of prob_j (that has the probabilities) in the position j the product of self.n (length of probs) and the item the list of probabilities in position j
            self.alias[j] = k                                       #append to the list of alias the variable k in the position j
            self.p[k] = self.p[k] + (self.p[j] - 1.0/self.n)        #append to the list of probabilities in position k the sum between the item of list of probabilities in position k plus the subtstraction of probability in position j minus the threshold 
            if self.p[k] > 1.0/self.n:       #check if the item of the list of probabilities in position k is bigger than the threshold 
                large[l] = k                 #the item is bigger, so set the item in the list large in position l to be k
                l += 1                       #the item is bigger, so add one to the variable l
            else:                            #if the item of the list of probabilities in position k is smaller it enters in this condition
                small[s] = k                 #the item is smaller, so set the item in the list small in position s to be k
                s += 1                       #the item is smaller, so add one to the variable s
        while s > 0:                         #initialize a while loop that will run while s is bigger than 0.
            s -= 1                           #substract 1 from the counter of the length of small list.
            self.prob_j[small[s]] = 1        #define the item of the list of probabilities in the position of small list in position s to 1
        while l > 0:                         #initialize a while loop that will run while l is bigger than 0.
            l -= 1                           #substract 1 from the counter of the length of large list. 
            self.prob_j[large[l]] = 1        #define the item of the list of probabilities in the position of large list in position l to 1


    def sample(self):                        #this function is used to produce a sample for the usage of the other functions
        i = random.randint(0, self.n-1)      #define i as a random integer between 0 and the length of the probability list-1
        r = random.uniform(0, 1)             #define r as a random uniform float between 0 and 1
        if r < self.prob_j[i]:               #this condition checks whether the float r is smaller than the item of the probability list in position i
            return i                         #if the condition is met, return i
        else:                                #if the condition is not met enter this instead
            return self.alias[i]             #return the item of the alias list in position i





def main():                                 #this is the main function that executes all the other function
    p = [0.1,0.2,0.2,0.5]                   #define a probability list called p
    alias = RandomMultinomial(p)            #define an alias list that is obtain from giving the list of probabilities as an input in the functio RandomMultinomial
    count = [0]*len(p)                      #define the count list as the length of the probability list times a 0 item in a list
    for i in range(100000):                 #initiate a for loop that iterates for i from 0 to 100000, so it will do the loop 100000 times
        j = alias.sample()                  #define variable j as the output of the function sample
        count[j] = count[j] + 1.0/100000.0  #set the item in the list count in position j as the item in count in position j plus 1/100000
    print(count)                            #print the list count to see the probabilities after 100000 iterations, they should be similar to the ones given as p due to the large number of iterations
    
    
if __name__ == "__main__":
    main()