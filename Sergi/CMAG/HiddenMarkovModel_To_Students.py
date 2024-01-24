'''
@author: olao
'''
from Script_Alias import RandomMultinomial

import math

'''
A class to code methods that are used in HMM.
'''
class HiddenMarkovModel(object):

    '''
    Create an object HiddenMarkovModel with transition states and emission probabilities for each state
    Transition is a dictionary where, for each state, we count the probability to move to another state
    Emission is a dictionary where, for each state, we store the probabilities of each category
    '''
    def __init__(self, transition, emission):
        if transition.__len__()!=emission.__len__():
            raise Exception("for each state, we must have an emission probability vector, but found " + transition.__len__() + " " + emission.__len__())        
        self.n = transition.__len__()
        self.transition = transition
        self.emission = emission
        '''
        dictionary to store the random multinomial 
        '''
        self.random_transition = {}
        self.random_emission = {}  
        
        '''
        Initialize the random multinomial
        '''
        for key in self.transition:
            self.random_transition[key] = RandomMultinomial(list(transition[key].values()))
            self.random_emission[key] = RandomMultinomial(list(emission[key].values()))
        
        
    '''
    Compute a sequence of length using a prior probabilities dictionary of the states to start the chain.
    Return the sequence and its hidden states
    '''    
    def generate_sequence(self, length_sequence, prior_probabilities):
        chain = []
        hidden_states = []
        '''
        Iterate over the i elements of the sequence, generating given the emission probabilities and transition probabilities a new .
        '''
        pr = RandomMultinomial(list(prior_probabilities.values()))
        state = list(prior_probabilities.keys())[pr.sample()]
        for i in range(length_sequence):
            '''
            from the state, use its emission probability to sample one element
            '''
            category = list(self.emission[state].keys())[self.random_emission[state].sample()]
            chain.append(category)
            hidden_states.append(state)
            state = list(self.transition[state].keys())[self.random_transition[state].sample()]
        output = [chain,hidden_states]
        return(output)
    
    
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
    # Initialize the forward probabilities with the prior probabilities.
        f_i = prior_probabilities.copy()
        
        # Initialize S
        S = 0

        # Iterate over each element in the observed sequence
        for i in range(len(sequence)):
            # Initialize a dictionary to store the forward probabilities at the current position.
            f_ii = {}
            
            # Iterate over possible states at the current position
            for key_ii in f_i:
                # Initialize the accumulated probability for the current state at the current position.
                a = 0
                
                # Iterate over possible states at the previous position
                for key_i in f_i:
                    # Accumulate the probability of transitioning from key_i to key_ii at the next position,
                    # multiplied by the stored forward probability at key_i
                    a = a + self.transition[key_i][key_ii] * f_i[key_i]

                # Multiply the accumulated probability by the emission probability of observing the symbol
                # at the current position for the current state
                a = a * self.emission[key_ii][sequence[i]]
                
                # Store the result in the dictionary of forward probabilities for the current position.
                f_ii[key_ii] = a

            # Update the forward probabilities for the next iteration.
            f_i = f_ii

        # Calculate the total probability 
        S = math.log(sum(f_i.values()))

        return S

    '''
    given a sequence generated by a HiddenMarkovModel object, estimate the emission probabilities
    of the different categories for each state
    '''
    
    def estimate_emission_probabilities(self, seq):
    # Start a dictionary to count the times of each category for each state.
        emission_count = {state: {category: 0 for category in self.emission[state]} for state in self.emission}

        # Iterate over pairs of observed categories and corresponding hidden states in the sequence.
        for category, state in zip(seq[0], seq[1]):
            # Sum up 1 for the given category and state.
            emission_count[state][category] += 1

        # Calculate emission probabilities 
        emission_probabilities = {state: {category: count / sum(emission_count[state].values())
                                        for category, count in emission_count[state].items()}
                                for state in self.emission}

        return emission_probabilities


     
    
    '''
    given a sequence generated by a HiddenMarkovModel object, estimate the transition probabilities
    between states
    '''    
    
    def estimate_transition_probabilities(self, seq):
        #Start a dictionary to count the transitions between states
        transition_count = {state: {next_state: 0 for next_state in self.transition[state]}
                            for state in self.transition}

        # Iterate through the states in the sequence to count
        for i in range(1, len(seq[1])):

            # Know the current state and the next state
            current_state = seq[1][i - 1]
            next_state = seq[1][i]
            
            # Sum the count of transitions from the current state to the next state
            transition_count[current_state][next_state] += 1

        # Calculate transition probabilities based on the counts
        transition_probabilities = {state: {next_state: count / sum(transition_count[state].values())
                                            for next_state, count in transition_count[state].items()}
                                    for state in self.transition}

        # Return the estimated transition probabilities
        return transition_probabilities


        
    


def main():
    transition_probability = {"S":{"S":0.9,"L":0.1},"L":{"S":0.2,"L":0.8}};
    emission_probability = {"S":{"G":0.1,"C":0.2,"T":0.2,"A":0.5}, "L":{"G":0.01,"C":0.1,"T":0.3,"A":0.59}}
    hmm = HiddenMarkovModel(transition_probability, emission_probability)
    
    prior_probability = {"S":0.5, "L":0.5}
    
    seq = hmm.generate_sequence(600, prior_probability)
    
    emission_prob = hmm.estimate_emission_probabilities(seq);
    
    for key in emission_prob:
        print(key, emission_prob[key])
        
    transition_prob = hmm.estimate_transition_probabilities(seq)
    
    for key in transition_prob:
        print(key, transition_prob[key])    
    
    print(hmm.log_probability_sequence_using_scaling(seq[0], prior_probability))

    print(hmm.log_probability_sequence_without_scaling(seq[0], prior_probability))


    
if __name__ == "__main__":
    main () 
