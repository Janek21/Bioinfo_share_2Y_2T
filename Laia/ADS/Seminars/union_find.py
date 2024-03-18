class OurUF(dict):
    def __init__(self):
        self.d = {}

    
    def new(self, x): # add a new entry in the diccionary. 
        self.d[x] = x
    

    def find(self, v): # returns the root.
        if self.d[v] == v:
            return v
        else:
            self.d[v] = self.find(self.d[v])
            return self.find(self.d[v])


    def union(self, x, y): # modifies the root of each child.
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.d[root_x] = root_y
    

    def get_dict(self):
        return self.d


def main():
    obj = OurUF()
    for i in range(6):
        obj.new(i)

    obj.union(3, 2)
    obj.union(4, 3)
    obj.union(2, 1)
    obj.union(5, 1)


    print(obj.find(4))
    print(obj.get_dict())

if __name__ == '__main__':
    main()
