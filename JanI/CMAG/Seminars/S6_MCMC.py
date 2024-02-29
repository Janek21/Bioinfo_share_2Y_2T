'''

@author: olao
'''
import math
import random

class MCMC(object):
    '''
    classdocs
    '''

    def __init__(self, values, initial_mean, sd): #take as input, a value list, a initial mena and a standard deviation
        self.values = values # define values so that it can be accessed by any method
        self.mean = initial_mean
        self.sd = sd
        self.previous_log_likelihood = self.compute_loglikelihood_Values(self.mean)
    
    
    def log_pdf_normal(self,x, mean): #calculates likelihood (if val x is compared to another value then lik says which is more probable)
        return (-0.5*((x-mean)/self.sd)**2)-math.log(self.sd*(2*math.pi)**0.5)
    
    def compute_loglikelihood_Values(self, mean):
        log_likelihood = 0
        for v in self.values:
            likelihood = self.log_pdf_normal(v, mean)
            log_likelihood += likelihood
        return log_likelihood
    
    def next_movement(self,sd_movement):
        return random.gauss(self.mean, sd_movement)
    
    def set_mean(self,new_mean):
        self.mean = new_mean
    
    def get_mean(self):
        return self.mean
    
    def metropolis_algorithm(self, sd_movement):

        pre=self.previous_log_likelihood #previous likelihood

        mv=self.next_movement(sd_movement) #generate movement (0.5=sd) (random num from gauss mean=current mean, sd=sd_movement)
        #new mean=mv ?

        #is mv valid to be new mean?

        curr_lik=self.compute_loglikelihood_Values(mv)
        
        ratio=curr_lik-pre #like doing curr_lik/pre (e^this)

        print("ratio", ratio)
 
        r=math.log(random.uniform(0,1)) #instead of exp in ratio
        
        if ratio>=r: #if ratio bigger than 1 or random chance define mv as the new mean
            self.set_mean(mv) # define the new mean as the result of the movement
            self.previous_log_likelihood=mv #??

        return self.mean         
    
    
def main():
    
    observed_seq = []
    
    mean = 5
    sd = 1
    
    for i in range(100):
        observed_seq.append(random.gauss(mean,sd))    
  
    mcmc_seq = []
    
    print(observed_seq)

    initial_mean =  random.uniform(-10,10)
    
   
    mcmc = MCMC(observed_seq, initial_mean, 1.0)
    
    for i in range(1000):
        print(mcmc.metropolis_algorithm(0.5))
    

    
    
if __name__ == "__main__":
    main () 
    
        


        