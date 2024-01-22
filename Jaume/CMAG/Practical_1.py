# Importing library to get random numbers
import random

# Creation of the class that will contain all the functions and atributes
class Random_Multinomial(object):
	
	# Initialization of the class and getting input from terminal
	def __init__(self, p):
		
		# Storing the value as an atribute of the class
		self.n = len(p) # n is the number of different events

		# Creation of the list that will store the event and each probability
		self.p = p

		# Creation of the lists to store alias and probabilities
		self.alias = [None] * self.n
		self.prob_j = [None] * self.n
		self.build_alias()
	
	# Function that will create the random distributions
	def build_alias(self):
		
		# Creation of both large and small lists
		large = []
		small = []

		# Storing the length of each list in 2 variables
		l = len(large)
		s = len(small)

		# Classification of prob in large or small
		for j in range(self.n):

			# If teh probability is bigger we put it in the large list
			if self.p[j] >= 1.0/self.n:
				large.append(j)
				l += 1

			# If is smaller in the small list
			else:
				small.append(j)
				s += 1
		
		# Creation of the alias:
		# While loop that will go on as long as the lengths of both lists are not 0
		while s != 0 and l != 0:
			'''
			Each loop will get us a value k and j from the lists small and big starting by the end
			and getting closser to the beggining through each iteration
			'''
			s -= 1 # Substraction of 1 from the index for small list
			l -= 1 # Substraction of 1 from the index for the large listl

			j = small[s] # Getting the value in position before the last iteration (the end for the 1st)
			k = large[l] # Getting the value in position before the last iteration (the end for the 1st)

			# Table creation
			self.prob_j[j] = self.n * self.p[j] # Computing n*pi (theory) and appending it in pos j from prob_j list
			self.alias[j] = k # Appending the value in position l of large list to alias list at position j
			self.p[k] = self.p[k] + (self.p[j] - 1.0/self.n) # Computing (value at position k of p list) + ((value at position j from p list) - 1/length of p) and storing the rsult in p at position k

			# Checking if the value at position k is bigger than 1/lenght of p
			if self.p[k] > 1.0/self.n:

				large[l] = k # Appending the item in position l of list large to itself
				l += 1 # Because we have substracted before 1 we need to 'neutralize' it

			# If not:
			else:
				
				small[s] = k # Appending the item in position l of the large list to small in position s
				s += 1 #  Because we have substracted before 1 we need to 'neutralize' it
		
		# Iterations that will continue until we reach the end off the samll sequence
		while s > 0:
			'''
			It checks only s so we know that the iteration will continue until the end of the sequence
			It follows the same functioning of going back as the anterior loop
			'''
			s -= 1 # Substracting 1 to the small index
			self.prob_j[small[s]] = 1 # Change of value in the small list to 1 (a pair is formed)
		
		# Iterations that will continue until we reach the end of the large sequence
		while l > 0:
			'''
			It checks only s so we know that the iteration will continue until the end of the sequence
			It follows the same functioning of going back as the anterior loop
			'''
			l -= 1 # Substracting 1 to the small index
			self.prob_j[large[l]] = 1 # Change of value in the small list to 1 (a pair is formed)

	# Function that will do the sampling
	def sample(self):

		# Getting aa random value between 0 and the length of p (n-1)
		i = random.randint(0, self.n-1)
		# Getting a random value between 0 and 1
		r = random.uniform(0, 1)

		# Checking if r is smaller than the probability stored in position i (i is a random value)
		if r < self.prob_j[i]:
			return i # returning i if it is the case		
		
		# If it is not the case:
		else:
			return self.alias[i]# Returns the alias in position i
'''
def check():
	p = [0.1, 0.2, 0.2, 0.5]
	alias = Random_Multinomial(p)
	count = [0] * len(p)
	for i in range(10000):
		j = alias.sample()
		count[j] = count[j] * (1.0 / 10000.0) 
		print(count)
'''

# Main function
def main():
	n = int(input('Enter the number of events: ')) # Getting input (total number of different events)
	print() # Formatting

	# List that consists of the probabilities
	p = [None] * n
	e = [None] * n

	# Loop to get all the events and each respective probability
	for i in range(n):
		event = input('Event name: ') # Getting the event name (as string)
		prob = float(input(f'Probability of {event}: ')) # Getting the probability for an event (as float)
		print() # Formatting

		# Storing the values from input in a list
		p[i] = prob
		e[i] = event
	
	# Creating an instance of the Random_Multinomial class
	alias = Random_Multinomial(p)
	
	# Doing the sapling by calling the sample function after initialiting the class
	sampled_event_index = alias.sample()

	# Output
	print(f"Sampled event: {e[sampled_event_index]}")

	#check()

# Exacution of the script
if __name__ == "__main__":
	main()