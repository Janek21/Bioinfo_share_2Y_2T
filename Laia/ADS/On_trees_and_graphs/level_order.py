from pytokr import pytokr

s = pytokr()
avoid_first_input = s()

class leveltraversal:
    def __init__(self):
        self.D = {}

    def readtree(self):
        root_value = int(s())
        if root_value == -1:
            return None
        else:
            left_subtree = self.readtree()
            right_subtree = self.readtree()
            return (root_value, left_subtree, right_subtree)

    def tree_height(self,root, level):
        if root is None:
            return 0
        if level not in self.D:
            self.D[level] = []
        x, left_height, right_height = root
        self.D[level].append(str(x))

        self.tree_height(left_height, level+1) 
        self.tree_height(right_height, level+1)
        return self.D


lt = leveltraversal()
input_tree = lt.readtree()
height_dict = lt.tree_height(input_tree, 0)
for lvl in height_dict:
    print(f"level {int(lvl)+1}: {' '.join(height_dict[lvl])}")
    