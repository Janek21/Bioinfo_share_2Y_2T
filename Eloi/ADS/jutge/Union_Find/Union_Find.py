class OurUF(dict):

    def new(self, x):
        self[x] = x
        return 
    
    def find(self, v):
        if self[v] != v:
           self[v] = self.find(self[v]) 
           return self.find(self[v])
        return v
    
    def union(self, x, y):
        x_pos, y_pos  = self.find(x), self.find(y)
        self[x_pos] = y_pos
        return
    
    def print_dict(self):
        print(self)
        return self

d= {}
for value in range(10):
    d[value] = value

uf = OurUF(d)

uf.find(7)
uf.union(5,6)
uf.union(5,9)
uf.union(8,7)
uf.union(7,6)
uf.print_dict()
