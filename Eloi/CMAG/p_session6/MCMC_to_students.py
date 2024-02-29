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

	def __init__(self, values, initial_mean, sd):
		self.values = values
		self.mean = initial_mean
		self.sd = sd
		self.previous_log_likelihood = self.compute_loglikelihood_Values(self.mean)
	
	
	def log_pdf_normal(self,x, mean):
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
	
	def metropolis_algorithm(self, sd_movement):  						# Define the Metropolis algorithm function
		
		new_mean = self.next_movement(sd_movement)						# Generate a new mean value for the next step using a Gaussian random
		log_likelihood = self.compute_loglikelihood_Values(new_mean)	# Compute the log likelihood of the new mean value
		log_ratio = log_likelihood - self.previous_log_likelihood		# Calculate the acceptance ratio using the difference in log likelihoods
		
		if math.log(random.random()) < log_ratio:						# Accept or reject the proposed mean value based on the acceptance ratio in log space
			self.set_mean(new_mean)										# If accepted, update the mean to the new value
			self.previous_log_likelihood = log_likelihood				# Update the previous log likelihood to the proposed log likelihood
			
		return self.mean												# Return the current mean


def main():
	
	observed_seq = []
	
	mean = 5
	sd = 1
	
	for i in range(100):
		observed_seq.append(random.gauss(mean,sd))    
  
	mcmc_seq = []
	
	initial_mean =  random.uniform(-10,10)
	
   
	mcmc = MCMC(observed_seq, initial_mean, 1.0)
	
	lista = []
	for i in range(1000):
		res = mcmc.metropolis_algorithm(0.5)
		print(res)
		lista.append(res)
	plt.plot(lista, color = 'black', label='L1')
	plt.show()

	
	
if __name__ == "__main__":
	main () 
	
		


		
