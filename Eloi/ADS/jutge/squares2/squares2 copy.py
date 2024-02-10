#import sys;x = sys.stdin.readline();print(''.join([f'{num%10}' if (num+1)%int(x)!=0 else f'{num%10}\n' for num in range(int(x)**2)]))


import random

class RandomMultinomial(object):

    # This class represents a random multinomial distribution generator using alias sampling.

    def __init__(self, p):
        # The constructor takes a probability distribution `p` as input.

        self.p = p  # Stores the input probability distribution.
        self.n = len(self.p)  # Stores the number of categories in the probability distribution.
        self.alias = [None] * self.n  # Creates an array of `n` None values for storing aliases.
        self.prob_j = [None] * self.n  # Creates an array of `n` None values for storing probabilities.
        self.build_alias()  # Builds the alias table and associated probabilities.

    # This function constructs an alias table for efficient random sampling.

    def build_alias(self):
        # Create two lists, `large` and `small`, to store indices with probabilities greater than or equal to 1.0 and less than 1.0, respectively.

        large = []
        small = []

        # Scale the probabilities by the number of categories.

        scaled_probabilities = [prob * self.n for prob in self.p]

        # Populate `large` and `small` lists based on scaled probabilities.

        for j in range(self.n):
            if scaled_probabilities[j] >= 1.0:
                large.append(j)
            else:
                small.append(j)

        # Construct the alias table and associated probabilities.

        while small and large:

            # Pick an index `l` from the `small` list with probability less than 1.0.

            l = small.pop()

            # Pick an index `g` from the `large` list with probability equal to the sum of the remaining probabilities.

            g = large.pop()

            # Store the probabilities for the current category.

            self.prob_j[l] = scaled_probabilities[l]

            # Set the alias for the current category.

            self.alias[l] = g

            # Update the probability of the 'g' category by adding the probability of the 'l' category and subtracting 1.0.

            scaled_probabilities[g] = scaled_probabilities[g] + scaled_probabilities[l] - 1.0

            # Place the updated 'g' category back into either `large` or `small` lists based on its new probability.

            if scaled_probabilities[g] >= 1.0:
                large.append(g)
            else:
                small.append(g)

        # Fill in the remaining None values in `prob_j` with scaled probabilities.

        for j in range(self.n):
            if self.prob_j[j] is None:
                self.prob_j[j] = scaled_probabilities[j]

    # This function generates a random sample from the multinomial distribution.

    def generate_sample(self):
        # Choose an index `i` uniformly from the range `[0, n - 1]`.

        i = random.randint(0, self.n - 1)

        # Compare the random value with the associated probability.

        if random.random() < self.prob_j[i]:
            # Return the index `i` if the random value is less than the probability.
            return i
        else:
            # Return the alias of index `i` if the random value is greater than the probability.
            return self.alias[i]


def main():
    # This is the main function for testing the RandomMultinomial class.

    # Define an example probability distribution `p`.

    p = [0.1, 0.2, 0.2, 0.5]

    # Create an instance of RandomMultinomial with the given probabilities `p`.

    alias = RandomMultinomial(p)

    # Initialize a count list `count` to track the frequency of each category.

    count = [0] * len(p)

    # Generate 100 samples and update the
