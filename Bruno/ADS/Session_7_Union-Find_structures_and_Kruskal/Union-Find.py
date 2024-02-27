class OurUF(dict):
    def __init__(self):
        self.parents = {}


    def make_set(self, x):
        self.parents[x] = -1
    
    def find(self, v):
        
        if self.parents[v] == -1:
            return v
        else:
            return self.find(self.parents[v])
    
    def union(self, x, y):
        if self.parents[y] == -1:
            self.parents[x] = y
        else:
            self.union(x, self.parents[y])


    
# Create an instance of the Union-Find class
uf = OurUF()

# Create individual sets
uf.make_set(1)
uf.make_set(2)
uf.make_set(3)
uf.make_set(4)

print(uf.parents)

# Perform union operations
uf.union(1, 2)
uf.union(3, 4)
uf.union(2, 3)

print(uf.parents)

# Verify if sets are merged correctly
print("Root of 1:", uf.find(1))  # Expecting the root to be 3
print("Root of 2:", uf.find(2))  # Expecting the root to be 3
print("Root of 3:", uf.find(3))  # Expecting the root to be 3
print("Root of 4:", uf.find(4))  # Expecting the root to be 3

# Verify if the disjoint sets are correctly maintained
print("Parents:", uf.parents)  # Expecting {1: 3, 2: 3, 3: 3, 4: 3}
