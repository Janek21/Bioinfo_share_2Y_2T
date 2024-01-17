import random

class RandomMultinomial(object):
    
    def __init__(self, p):
        # Step 0: Begin with  the RandomMultinomial class with a probability distribution 'p'
        self.p = p
        self.n = len(self.p)
        # Start arrays to store the alias and scaled probabilities
        self.alias = [None] * self.n
        self.prob_j = [None] * self.n
        # Build the alias tables during the programm
        self.build_alias()

    def build_alias(self):
        large = []
        small = []

        # Step 1: Start lists and scaled probabilities
        for j in range(self.n):
            self.prob_j[j] = self.p[j] * self.n
            # Separate into 'large' and 'small' lists based on scaled probability
            if self.prob_j[j] >= 1.0:
                large.append(j)
            else:
                small.append(j)

        # Step 2: Build the alias tables
        while large and small:
            l = small.pop()
            g = large.pop()

            # Assign alias and update scaled probability for the 'small' value
            self.alias[l] = g
            self.prob_j[g] = self.prob_j[g] - (1 - self.prob_j[l])

            # Reorganize into 'large' or 'small' based on the updated scaled probability
            if self.prob_j[g] >= 1.0:
                large.append(g)
            else:
                small.append(g)

    def sample(self):
        # Step 3: Generate a random sample
        i = random.randint(0, self.n - 1)
        r = random.uniform(0, 1)

        # Compare with scaled probability to determine the sample
        if r < self.prob_j[i]:
            return i
        else:
            return self.alias[i]

def main():    
    p = [0.1, 0.2, 0.2, 0.5]    
    alias = RandomMultinomial(p)
    count = [0] * len(p)

    # Step 4: Generate samples and update counts
    for i in range(100000):
        j = alias.sample()
        count[j] += 1.0 / 100000.0

    # Step 5: Print the normalized counts
    print(count)

if __name__ == "__main__":
    main()
