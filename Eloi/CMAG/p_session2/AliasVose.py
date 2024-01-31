import random

class RandomMultinomial(object):

    def __init__(self, p):												# Initialize the RandomMultinomial class with a probability distribution 'p'.
        self.p = p  													# Declaring the probability distribution using self parameter
        self.n = len(self.p)  											# Number of possibilities in the prob. distribution, in this case A,C,T,G = 4
        self.alias = [None] * self.n  									# Alias table for efficient random sampling
        self.prob_j = [None] * self.n									# Probability values for each category in the alias table
        self.build_alias()  											# Build the alias table during initialization

    def build_alias(self):												# Build the alias table and associated probabilities.
        large = []  													# List to store indices with probabilities greater than or equal to 1.0
        small = []  													# List to store indices with probabilities less than 1.0
        scaled_probabilities = [prob * self.n for prob in self.p]  		# Scale probabilities by the number of categories

        for j in range(self.n):											# Populate the 'large' and 'small' lists based on scaled probabilities.
            if scaled_probabilities[j] >= 1.0:
                large.append(j)
            else:
                small.append(j)

        while small and large:											# Construct the alias table and associated probabilities.
            l = small.pop()  											# Index with probability less than 1.0
            g = large.pop()  											# Index with probability greater than or equal to 1.0

            self.prob_j[l] = scaled_probabilities[l]  					# Set probability for category 'l'
            self.alias[l] = g  											# Set alias for category 'l'

            scaled_probabilities[g] = scaled_probabilities[g] + scaled_probabilities[l] - 1.0  # Update scaled probability

            if scaled_probabilities[g] >= 1.0:
                large.append(g)
            else:
                small.append(g)

        for j in range(self.n):											# Initialize remaining None values in prob_j with scaled probabilities.
            if self.prob_j[j] is None:
                self.prob_j[j] = scaled_probabilities[j]

    def sample(self):											# Generate a random sample from the multinomial distribution.
        i = random.randint(0, self.n - 1)  								# Randomly choose an index 'i'
        if random.random() < self.prob_j[i]:  							# Compare with associated probability
            return i
        else:
            return self.alias[i] 										# Return the alias if the random value is greater than the probability

def main():																# Main function for testing the RandomMultinomial class.
    p = [0.1, 0.2, 0.2, 0.5]  											# Example probability distribution
    alias = RandomMultinomial(p)  										# Create an instance of RandomMultinomial with the given probabilities
    count = [0] * len(p)  												# Initialize a count list to track the frequency of each category

    for _ in range(100):												# Generate samples and update the count list.
        j = alias.generate_sample()  									# Generate a random sample
        count[j] += 1.0 / 100.0  									# Update the count for the chosen category

    print(count)  														# Print the normalized count list

if __name__ == "__main__":												# Run the main function if this script is executed directly.
    main()
