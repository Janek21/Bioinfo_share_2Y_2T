'''
@author: Eloi
'''
from AliasVose import RandomMultinomial  								# Import the RandomMultinomial class from AliasVose module
import math  															# Import the math module
'''
A class to code methods that are used in HMM.
'''
class HiddenMarkovModel(object):										# HiddenMarkovModel class definition
	'''
	Create an object HiddenMarkovModel with transition states and emission probabilities for each state
	Transition is a dictionary where, for each state, we count the probability to move to another state
	Emission is a dictionary where, for each state, we store the probabilities of each category
	'''
	def __init__(self, transition, emission):							# Constructor to initialize the HMM object
		if transition.__len__() != emission.__len__():  				# Check if the lengths of transition and emission dictionaries are not equal
			raise Exception("for each state, we must have an emission probability vector, but found " + transition.__len__() + " " + emission.__len__())  # Raise an exception with a descriptive message if lengths are not equal
		self.n = transition.__len__()  									# Set the number of states
		self.transition = transition  									# Set the transition probabilities
		self.emission = emission  										# Set the emission probabilities
		'''
		dictionary to store the random multinomial 
		'''
		self.random_transition = {}  									# Dictionary to store RandomMultinomial instances for transitions
		self.random_emission = {}  										# Dictionary to store RandomMultinomial instances for emissions
		'''
		Initialize the random multinomial
		'''
		for key in self.transition:  									# Iterate over each state in the transition dictionary
			self.random_transition[key] = RandomMultinomial(list(transition[key].values()))  # Create RandomMultinomial instance for transition based on the probability values
			self.random_emission[key] = RandomMultinomial(list(emission[key].values()))  # Create RandomMultinomial instance for emission based on the probability values
	'''
	Compute a sequence of length using a prior probabilities dictionary of the states to start the chain.
	Return the sequence and its hidden states
	'''    
	def generate_sequence(self, length_sequence, prior_probabilities):  # Define a method to generate a sequenceusing prior probabilities
		chain = []  													# List to store the generated sequence
		hidden_states = []  											# List to store the hidden states of the sequence
		'''
		Iterate over the i elements of the sequence, generating given the emission probabilities and transition probabilities a new .
		'''
		pr = RandomMultinomial(list(prior_probabilities.values()))  	# Create a RandomMultinomial instance for initial state
		state = list(prior_probabilities.keys())[pr.sample()]  			# Sample the initial state
		for i in range(length_sequence):								# Iterate over every position in the sequence
			'''
			from the state, use its emission probability to sample one element
			'''
			category = list(self.emission[state].keys())[self.random_emission[state].sample()]  # Sample the category based on emission probabilities
			chain.append(category)  									# Append the sampled category to the sequence
			hidden_states.append(state)  								# Append the current state to the hidden states
			state = list(self.transition[state].keys())[self.random_transition[state].sample()]  # Transition to a new state
		output = [chain, hidden_states]  								# Output the generated sequence and its hidden states
		return output													# Return output 
	'''
	Compute the log probability of the sequence using forward algorithm. It uses the scale algorithm (Rabiner) to prevent underflow
	'''
	def log_probability_sequence_using_scaling(self, sequence, prior_probabilities): # Define method to compute log probability of a sequence using scaling
		f_i = prior_probabilities.copy()  								# Initialize the forward probabilities with the prior probabilities
		S = 0  															# Initialize the log probability accumulator		
		
		for i in range(len(sequence)):									# Iterate over every position of the sequence
			s_ii = 0  													# Initialize the scaling factor
			f_ii = {}  													# Dictionary to store the updated forward probabilities
			
			for key_ii in f_i:											# Iterate over the hidden states for the current position
				a = 0  													# Initialize the accumulator for forward probabilities	
				
				for key_i in f_i:										# Iterate over the previous hidden states
					a = a + self.transition[key_i][key_ii] * f_i[key_i] # Update the forward probability using transition probabilities
				a = a * self.emission[key_ii][sequence[i]]  			# Update the forward probability using emission probabilities
				f_ii[key_ii] = a  										# Store the updated forward probability
				s_ii = s_ii + a  										# Update the scaling factor
				
			for key_ii in f_ii:											# Normalize the forward probabilities using the scaling factor
				f_i[key_ii] = f_ii[key_ii]/s_ii  		  				# Update each forward probability by dividing it by the scaling factor
			S = S + math.log(s_ii)  									# Accumulate the log probability using the scaled factor
		
		return S  														# Return the log probability



	def log_probability_sequence_without_scaling(self, sequence, prior_probabilities): # Method to compute log probability of a sequence without scaling
		f_i = prior_probabilities.copy()  								# Initialize the forward probabilities with the prior probabilities
		S = 0 															# Initialize the log probability accumulator

		for i in range(len(sequence)):									# Iterate over every position of the sequence
			f_ii = {}  													# Dictionary to store the updated forward probabilities
			
			for key_ii in f_i:											# Iterate over the hidden states for the current position
				a = 0  													# Initialize the accumulator for forward probabilities
				
				for key_i in f_i:										# Iterate over the previous hidden states
					a = a + self.transition[key_i][key_ii] * f_i[key_i] # Update the forward probability using transition probabilities

				a = a * self.emission[key_ii][sequence[i]]  			# Update the forward probability using emission probabilities
				f_ii[key_ii] = a 										# Store the updated forward probability

			f_i = f_ii  												# Update the forward probabilities

		S = math.log(sum(f_i.values()))  								# Calculate the log probability without scaling

		return S  														# Return the log probability

	
	'''
	given a sequence generated by a HiddenMarkovModel object, estimate the emission probabilities
	of the different categories for each state
	'''
	def estimate_emission_probabilities(self, seq):						# Method to estimate emission probabilities from a generated sequence
		prob_dict = {"S": {"G": 0, "C": 0, "T": 0, "A": 0}, "L": {"G": 0, "C": 0, "T": 0, "A": 0}}  # Initialize the emission probability dictionary
		nucs = seq[0]  													# Extract the generated sequence
		states = seq[1]  												# Extract the hidden states of the sequence
		for pos in range(len(nucs)):									# Iterate over each postion of the sequence					
			prob_dict[states[pos]][nucs[pos]] += 1  					# Update the dictionnary based on the state and the nucleotide on the position of the sequence
		
		for key_1 in prob_dict.keys():									# Calculate each emission prob. for each state, to do that we iterate over each state
			sum_values = sum(prob_dict[key_1].values())  				# Calculate the sum of values to normalize the values
			
			for key_2 in prob_dict[key_1].keys():						# Iterate for every nucleotide to normalize
				if prob_dict[key_1][key_2] != 0:						# Check if nucleotide frequency is 0, because you cannot divide 0
					prob_dict[key_1][key_2] = prob_dict[key_1][key_2]/sum_values  # Normalize the emission probabilities
					
		return prob_dict  												# Return the normalized estimated emission probabilities
	
	'''
	given a sequence generated by a HiddenMarkovModel object, estimate the transition probabilities
	between states
	'''    
	def estimate_transition_probabilities(self, seq): 					# Method to estimate transition probabilities from a generated sequence
		states = seq[1]  												# Extract the hidden states of the sequence
		trans_dict = {"S": {"S": 0, "L": 0}, "L": {"S": 0, "L": 0}}  	# Initialize the transition probability dictionary
		for pos in range(len(states)-1):								# Iterate over each position of the states sequence
			trans_dict[states[pos]][states[pos+1]] += 1  				# Update the transition probabilities based on the following character
			
		for key_1 in trans_dict.keys():									# Iterate over every hidden state to normalize correctly
			sum_values = sum(trans_dict[key_1].values())  				# Calculate the sum of values for normalization
			
			for key_2 in trans_dict[key_1].keys():						# Iterate for every states transition frequency to normalize into porbability
				if trans_dict[key_1][key_2] != 0:						# Check if state frequency is 0. Because if so, we would have fatal error
					trans_dict[key_1][key_2] = trans_dict[key_1][key_2]/sum_values  # Normalize the transition probabilities
					
		return trans_dict  												# Return the estimated transition probabilities

def main():																# Main function
	transition_probability = {"S": {"S": 0.9, "L": 0.1}, "L": {"S": 0.2, "L": 0.8}} # Define transition probabilities 
	emission_probability = {"S": {"G": 0.1, "C": 0.2, "T": 0.2, "A": 0.5}, "L": {"G": 0.01, "C": 0.1, "T": 0.3, "A": 0.59}} # Define emission probabilities
	
	hmm = HiddenMarkovModel(transition_probability, emission_probability)# Create HiddenMarkovModel object
	
	prior_probability = {"S": 0.5, "L": 0.5}							# Define prior probabilities
	
	seq = hmm.generate_sequence(600, prior_probability)					# Generate a sequence using the HMM
	
	emission_prob = hmm.estimate_emission_probabilities(seq)			# Estimate emission probabilities from the generated sequence

	for key in emission_prob:											# Iterate over every key
		print(key, emission_prob[key])									# Print every key with its emission probability
		
	transition_prob = hmm.estimate_transition_probabilities(seq)		# Print emission probabilities
	

	for key in transition_prob:											# Iterate over every key
		print(key, transition_prob[key]) 								# Print every key with its transition probability

	print(hmm.log_probability_sequence_using_scaling(seq[0], prior_probability))# Print log probability of the sequence using scaling

	print(hmm.log_probability_sequence_without_scaling(seq[0], prior_probability))	# Print log probability of the sequence without scaling

if __name__ == "__main__": 												# Check if the script is executed
	main () 															# Execute the main function
