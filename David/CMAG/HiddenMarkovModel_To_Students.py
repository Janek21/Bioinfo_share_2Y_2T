'''
@author: olao
'''
from Practical1 import RandomMultinomial

import math

'''
A class to code methods that are used in HMM.
'''
class HiddenMarkovModel(object):         #Define the class that will contain all the necesary functions for this program that computes the hidden markov model 

    '''
    Create an object HiddenMarkovModel with transition states and emission probabilities for each state
    Transition is a dictionary where, for each state, we count the probability to move to another state
    Emission is a dictionary where, for each state, we store the probabilities of each category
    '''
    def __init__(self, transition, emission):                #Define the initializer function that will take the self, the transition probabilities and emision probabilities as input
        if transition.__len__()!=emission.__len__():         #Create a condition if the transition matrix and emision matrix are of different length 
            raise Exception("for each state, we must have an emission probability vector, but found " + transition.__len__() + " " + emission.__len__())   #If they are of different length, raise an exception because the hidden markov model cannot be constructed       
        self.n = transition.__len__()               #define the variable self.n to be the length of the transition probability matrix
        self.transition = transition                #define the variable self.transition to be the transition probability matrix
        self.emission = emission                    #define the variable self.emission to be the emission probability matrix
        '''
        dictionary to store the random multinomial 
        '''
        self.random_transition = {}                 #define the self.random_transition to be an empty dictionary that later will store the new transition probabilities of the random multinomial
        self.random_emission = {}                   #define the self.random_emission to be an empty dictionary that later will store the new emission probabilities of the random multinomial
        
        '''
        Initialize the random multinomial
        '''
        for key in self.transition:                 #initialize a for loop that will iterate in every key of the transition probability dictionary and will use key as variable
            self.random_transition[key] = RandomMultinomial(list(transition[key].values()))  #define in the empty dictionary of transition as the key variable 'key' the output of the RandomMultinomial function with inputs the values of the transition probability dictionary for key 'key'
            self.random_emission[key] = RandomMultinomial(list(emission[key].values()))      #define in the empty dictionary of emission as the key variable 'key' the output of the RandomMultinomial function with inputs the values of the emission probability dictionary for key 'key'
        
        
    '''
    Compute a sequence of length using a prior probabilities dictionary of the states to start the chain.
    Return the sequence and its hidden states
    '''    
    def generate_sequence(self, length_sequence, prior_probabilities):     #define a function that will generate a random sequence given as inputs the class self, the length of the desired sequence and the prior probabilities of the nucleotides
        chain = []             #define chain as a empty list, this will contain the sequence
        hidden_states = []     #define hidden_states as an empty list that will contain the hidden markov states
        '''
        Iterate over the i elements of the sequence, generating given the emission probabilities and transition probabilities a new .
        '''
        pr = RandomMultinomial(list(prior_probabilities.values()))   #define pr as the output of the RandomMultinomial given as input the list of the values of the prior_probabilities input
        state = list(prior_probabilities.keys())[pr.sample()]        #define state as a list of the keys of the prior probabilities in the position of a random sample of the previous variable pr
        for i in range(length_sequence):                #start a for loop that will give a variable i every value from 0 to the desired length of the sequence
            '''
            from the state, use its emission probability to sample one element
            '''
            category = list(self.emission[state].keys())[self.random_emission[state].sample()]    #define the variable category as a list of the keys of the emission dictionary in the position of hte state in the position of  a random sample of the random_emission dictionary in the position state
            chain.append(category)                                                                #append to the chain list the category variable
            hidden_states.append(state)                                                           #append to the hidden states list the state variable
            state = list(self.transition[state].keys())[self.random_transition[state].sample()]   #define the variable category as a list of the keys of the transition dictionary in the position of hte state in the position of  a random sample of the random_transition dictionary in the position state
        output = [chain,hidden_states]                                                            #define as output a list with the chain in position 0 and the hidden states in position 1
        return(output)                                                                            #return the output
    
    
    '''
    Compute the log probability of the sequence using forward algorithm. It uses the scale algorithm (Rabiner) to prevent underflow
    '''
    def log_probability_sequence_using_scaling(self, sequence, prior_probabilities):  
        '''
        scaling factor
        '''
        f_i = prior_probabilities.copy()

        '''
        the probability turns out to be the multiplication of the scaling factor.
        Since we will use the log, it is the sum of the log of the scaling factor.
        Since the initial s0 adds to 1, the log of it is 0. We do not need to do anything else        
        '''
        S = 0
        
        for i in range(len(sequence)):
            s_ii = 0
            f_ii = {}
            '''
            comes from i
            '''
            for key_ii in f_i:
                '''
                goes to ii
                '''
                a = 0
                for key_i in f_i:
                    '''
                    probability that I move from key_i to key_ii in the position i+1
                    multiplied by the stored scaled f_i at key i 
                    '''
                    a = a + self.transition[key_i][key_ii]*f_i[key_i]
                
                '''
                Probability of, being at key_ii getting the category observed at sequence i
                '''
                a = a*self.emission[key_ii][sequence[i]]
                '''
                before re-scaling by the total s_ii
                '''
                f_ii[key_ii] = a
                '''
                Update the s_ii
                '''
                s_ii = s_ii + a
                
            '''
            Once we have computed all the f_ii, we need to re_scale by the s_ii and set this as the new f_i
            '''        
            for key_ii in f_ii:
                f_i[key_ii] = f_ii[key_ii]/s_ii            
           
            S = S + math.log(s_ii)
        
        return(S)
        
        

    '''
    Compute the log probability of the sequence using forward algorithm.
    '''    
    def log_probability_sequence_without_scaling(self, sequence, prior_probabilities):
        '''
        scaling factor
        '''
        f_i = prior_probabilities.copy()

        '''
        the probability turns out to be the multiplication of the scaling factor.
        Since we will use the log, it is the sum of the log of the scaling factor.
        Since the initial s0 adds to 1, the log of it is 0. We do not need to do anything else        
        '''
        S = 0
        
        for i in range(len(sequence)):
      
            f_ii = {}
            '''
            comes from i
            '''
            for key_ii in f_i:
                '''
                goes to ii
                '''
                a = 0
                for key_i in f_i:
                    '''
                    probability that I move from key_i to key_ii in the position i+1
                    multiplied by the stored scaled f_i at key i 
                    '''
                    a = a + self.transition[key_i][key_ii]*f_i[key_i]
                
                '''
                Probability of, being at key_ii getting the category observed at sequence i
                '''
                a = a*self.emission[key_ii][sequence[i]]
                '''
                before re-scaling by the total s_ii
                '''
                f_ii[key_ii] = a

            f_i = f_ii
            
                
            '''
            Once we have computed all the f_ii, we need to re_scale by the s_ii and set this as the new f_i
            '''        
             
           
            S = math.log(sum(f_i.values()))
        
        return(S)


    def estimate_emission_probabilities(self,seq):
        e = {}
        for state, obs in zip(seq[1], seq[0]):
            if state not in e:
                e[state] = {}
            if obs not in e[state]:
                e[state][obs] = 0
            e[state][obs] += 1

        for state in e:
            total = sum(e[state].values())
            for obs in e[state]:
                e[state][obs] /= total

        return e
        
    
    
  
    def estimate_transition_probabilities(self,seq):
        t = {}
        for i in range(len(seq[1]) - 1):
            state = seq[1][i]
            next_state = seq[1][i+1]
            if state not in t:
                t[state] = {}
            if next_state not in t[state]:
                t[state][next_state] = 0
            t[state][next_state] += 1

        for state in t:
            total = sum(t[state].values())
            for next_state in t[state]:
                t[state][next_state] /= total

        return t

        


def main():
    transition_probability = {"S":{"S":0.9,"L":0.1},"L":{"S":0.2,"L":0.8}};
    emission_probability = {"S":{"G":0.1,"C":0.2,"T":0.2,"A":0.5}, "L":{"G":0.01,"C":0.1,"T":0.3,"A":0.59}}
    hmm = HiddenMarkovModel(transition_probability, emission_probability)
    
    prior_probability = {"S":0.5, "L":0.5}
    
    seq = hmm.generate_sequence(10000, prior_probability)
    
    emission_prob = hmm.estimate_emission_probabilities(seq);
    
    for key in emission_prob:
        print(key, emission_prob[key])
        
    transition_prob = hmm.estimate_transition_probabilities(seq)
    
    for key in transition_prob:
        print(key, transition_prob[key])    
    
    #print(hmm.log_probability_sequence_using_scaling(seq[0], prior_probability))

    #print(hmm.log_probability_sequence_without_scaling(seq[0], prior_probability))


    
if __name__ == "__main__":
    main ()
