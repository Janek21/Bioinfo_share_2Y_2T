'''

@author: olao
'''
import math
import random
import matplotlib.pyplot as plt

class MCMC(object):
    '''
    classdocs
    '''

    def __init__(self, values, initial_mean, sd): # take as input, a value list, a initial mean and a standard deviation
        self.values = values # define values so that it can be accessed by any method
        self.mean = initial_mean # define a mean to be accessed by any method
        self.sd = sd # define sd to be accessed by ant method
        self.previous_log_likelihood = self.compute_loglikelihood_Values(self.mean) #set up a log likelyhood for the initial mean
    
    
    def log_pdf_normal(self,x, mean): #calculates likelihood (if val x is compared to another value then likelyhood says which is more probable)
        return (-0.5*((x-mean)/self.sd)**2)-math.log(self.sd*(2*math.pi)**0.5)
    
    def compute_loglikelihood_Values(self, mean): #calculates the log likelihood values for a given input
        log_likelihood = 0
        for v in self.values: #iterate over all values given as class input
            likelihood = self.log_pdf_normal(v, mean) #calculates the likelihood for the current value
            log_likelihood += likelihood #adds the calculated likelihood to the total
        return log_likelihood #returns the calculated likelihood
    
    def next_movement(self,sd_movement): #returns a random number from the mean to the input variable using a Gaussian random generation
        return random.gauss(self.mean, sd_movement)
    
    def set_mean(self,new_mean): #set a new self.mean
        self.mean = new_mean
    
    def get_mean(self): #outputs the current self.mean
        return self.mean
    
    def metropolis_algorithm(self, sd_movement):

        pre=self.previous_log_likelihood #define previous likelihood

        n_mean=self.next_movement(sd_movement) #generate a new random mean (0.5=sd) (random num from gauss mean=current mean, sd=sd_movement)
        curr_lik=self.compute_loglikelihood_Values(n_mean) #get logLikelyhood of the new mean
        
        ratio=curr_lik-pre #use the difference in likelyhoods to calculate a ratio
 
        r=math.log(random.uniform(0,1)) #instead of doing e^ratio
        
        if ratio >= r: #if ratio bigger than 1 or random chance define n_mean as the new mean
            self.set_mean(n_mean) #define the new mean as the result of the movement
            self.previous_log_likelihood=curr_lik #update the previous log likelyhood to the current one

        return self.mean #return the current mean   
    
    
def main():
    
    observed_seq = []
    
    mean = 5
    sd = 1
    
    for i in range(100):
        observed_seq.append(random.gauss(mean,sd)) #add 100 gaussian random values between the mean and sd
  
    mcmc_seq = []
    
    print(observed_seq)
    initial_mean =  random.uniform(-10,10) #define an initial mean as a float between -10 and 10
    
    mcmc = MCMC(observed_seq, initial_mean, 1.0)
    
    for _ in range(1000): #add 1000 values to mcmc_seq calculated with the metropolis algorithm and using the 100 values in observed_sequences as values for the computation
        sol=mcmc.metropolis_algorithm(0.5)
        mcmc_seq.append(sol)
    
    print(mcmc_seq) #print the Montecarlo markov chains

    plt.plot(mcmc_seq) #plot the list for a better comprehension (no necessari)
    plt.xlabel("Computation")
    plt.show()


    
    
if __name__ == "__main__":
    main () 
    
        


        