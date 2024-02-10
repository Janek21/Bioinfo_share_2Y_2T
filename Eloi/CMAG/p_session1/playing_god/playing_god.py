import random															# Importing random library for random sampling
																		# Line break for stuctural purposes
class RandomMultinomial(object):										# Define class random multinomial distributon
																		# Line with lots of \t
    def __init__(self, p):												# Define the constructor takes a probability distribution `p` as input.
        self.p = p  													# Declaring the probability distribution using self parameter
        self.n = len(self.p)  											# Number of possibilities in the prob. distribution, in this case A,C,T,G = 4
        self.alias = [None] * self.n  									# Creates an array of `n` None values for storing aliases.
        self.prob_j = [None] * self.n									# Creates an array of `n` None values for storing probabilities.
        self.build_alias()  											# Build the alias table during initialization
																		# Line break
    def build_alias(self):												# Define function to build the alias table and associated probabilities.
        large = []  													# List to store indices with probabilities greater than or equal to 1.0
        small = []  													# List to store indices with probabilities less than 1.0
        scaled_probabilities = [prob * self.n for prob in self.p]  		# Scale probabilities by the number of categories
																		# Line Break
        for j in range(self.n):											# Populate the 'large' and 'small' lists based on scaled probabilities.
            if scaled_probabilities[j] >= 1.0:							# Conditional for filtering scaled probabilities to large list
                large.append(j)											# Append filtered scaled probability to large list
            else:														# Conditional for filtering to small list
                small.append(j)											# Append filtered scaled probability to small list
																		# Line break 
        while small and large:											# While small and large are not empty
            l = small.pop()  											# Pick an index `l` from the `small` list with probability less than 1.0.
            g = large.pop()  											# Pick an index `g` from the `large` list with probability equal to the sum of the remaining probabilities.
																		# Line with a lot of \t
            self.prob_j[l] = scaled_probabilities[l]  					# Store the probabilities for the current category.
            self.alias[l] = g  											# Set the alias for the current category.
																		# Line break
            scaled_probabilities[g] = scaled_probabilities[g] + scaled_probabilities[l] - 1.0  # Update the probability of the 'g' category by adding the probability of the 'l' category and subtracting 1.0.
																		# Line breal
            if scaled_probabilities[g] >= 1.0:							# Conditional to place the updated 'g' category back into `large` based on its new updated probability
                large.append(g)											# Append updated 'g' into large
            else:														# Conditional to place the updated 'g' category back into `small` based on its new updated probability
                small.append(g)											# Append updated 'g' into small
																		# Line break
        for j in range(self.n):											# Iterate over positions in array prob_j
            if self.prob_j[j] is None:									# Detect if position in array has None value
                self.prob_j[j] = scaled_probabilities[j]				# If position has none value, fill it with scaled probabilities
																		# Line break
    def generate_sample(self):											# Define function to generate a random sample from the multinomial distribution.
        i = random.randint(0, self.n - 1)  								# Randomly choose an index 'i'
        if random.random() < self.prob_j[i]:  							# Compare with associated probability
            return i													# Return the index `i` if the random value is less than the probability.
        else: return self.alias[i] 										# Return the alias of index `i` if the random value is greater than the probability.
																		# Line break
def main():																# Main function for testing the RandomMultinomial class.
    p = [0.1, 0.2, 0.2, 0.5]  											# Define an example probability distribution `p`.
    alias = RandomMultinomial(p)  										# Create an instance of RandomMultinomial with the given probabilities
    count = [0] * len(p)  												# Initialize a count list to track the frequency of each category
																		# Line break
    for _ in range(100):												# Generate samples and update the count list.
        j = alias.generate_sample()  									# Generate a random sample from the multinomial distribution
        count[j] += 1.0 / 100.0  										# Update the count for the chosen category
    print(count)  														# Print the normalized count list
																		# Last line break
if __name__ == "__main__":  											# Check if the script is being executed directly
    main()  															# Call the main function
