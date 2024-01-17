import random

class RandomMultinomial(object):
    '''
    Constructor
    '''
    def __init__(self, p):
        self.p = p
        self.n = len(self.p)
        self.alias = [None] * self.n
        self.prob_j = [None] * self.n
        self.build_alias()

    def build_alias(self):
        large = []
        small = []
        l = len(large)
        s = len(small)
        for j in range(self.n):
            if self.p[j] >= 1.0/self.n:
                large.append(j)
                l += 1
            else:
                small.append(j)
                s += 1
        while s != 0 and l != 0:
            s -= 1
            j = small[s]
            l -= 1
            k = large[l]
            self.prob_j[j] = self.n * self.p[j] 
            self.alias[j] = k
            self.p[k] = self.p[k] + (self.p[j] - 1.0/self.n)
            if self.p[k] > 1.0/self.n:
                large[l] = k
                l += 1
            else:
                small[s] = k
                s += 1
        while s > 0:
            s -= 1
            self.prob_j[small[s]] = 1
        while l > 0:
            l -= 1
            self.prob_j[large[l]] = 1


    def sample(self):
        i = random.randint(0, self.n-1)
        r = random.uniform(0, 1)
        if r < self.prob_j[i]:
            return i
        else:
            return self.alias[i]





def main():    
    p = [0.1,0.2,0.2,0.5]    
    alias = RandomMultinomial(p)
    count = [0]*len(p)
    for i in range(100000):
        j = alias.sample()
        count[j] = count[j] + 1.0/100000.0
    print(count)
    
    
if __name__ == "__main__":
    main()