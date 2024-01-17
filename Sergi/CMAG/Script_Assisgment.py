import random

class RandomMultinomial(object):
    
    def __init__(self, p):
        self.p = p
        self.n = len(self.p)
        self.alias = [None] * self.n
        self.prob_j = [None] * self.n
        self.build_alias()

    def build_alias(self):
        large = []
        small = []
        scaled_probabilities = [prob * self.n for prob in self.p]

        for j in range(self.n):
            if scaled_probabilities[j] >= 1.0:
                large.append(j)
            else:
                small.append(j)

        while small and large:
            l = small.pop()
            g = large.pop()

            self.prob_j[l] = scaled_probabilities[l]
            self.alias[l] = g

            scaled_probabilities[g] = scaled_probabilities[g] + scaled_probabilities[l] - 1.0

            if scaled_probabilities[g] >= 1.0:
                large.append(g)
            else:
                small.append(g)

        # Initialize remaining None values in prob_j
        for j in range(self.n):
            if self.prob_j[j] is None:
                self.prob_j[j] = scaled_probabilities[j]

    def generate_sample(self):
        i = random.randint(0, self.n - 1)
        if random.random() < self.prob_j[i]:
            return i
        else:
            return self.alias[i]

def main():    
    p = [0.1, 0.2, 0.2, 0.5]    
    alias = RandomMultinomial(p)
    count = [0] * len(p)

    for _ in range(100000):
        j = alias.generate_sample()
        count[j] += 1.0 / 100000.0

    print(count)

if __name__ == "__main__":
    main()
