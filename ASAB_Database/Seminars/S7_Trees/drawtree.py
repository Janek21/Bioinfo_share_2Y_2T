from Bio import Phylo
import sys

try:
    tree = Phylo.read(sys.argv[1], "newick")
except IndexError:
    print("program requires as file")
    sys.exit()
except FileNotFoundError:
    print(f"File {sys.argv[1]} not found")
    sys.exit()
Phylo.draw_ascii(tree)
