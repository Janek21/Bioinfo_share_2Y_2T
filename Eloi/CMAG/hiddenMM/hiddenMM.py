import random
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, _Matrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Phylo

# Function to generate a random DNA sequence
def generate_random_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

# Function to calculate the Jukes-Cantor distance between two sequences
def jukes_cantor_distance(seq1, seq2):
    L = len(seq1)
    differences = sum(1 for s1, s2 in zip(seq1, seq2) if s1 != s2)
    p = differences / L
    return -0.75 * np.log(1 - (4/3) * p)

# Generate random DNA sequences
num_sequences = 5
seq_length = 10
sequences = [SeqRecord(Seq(generate_random_sequence(seq_length)), id=f'Seq{i+1}') for i in range(num_sequences)]

# Create a distance matrix
distance_matrix = np.zeros((num_sequences, num_sequences))
for i in range(num_sequences):
    for j in range(i + 1, num_sequences):
        distance_matrix[i, j] = jukes_cantor_distance(str(sequences[i].seq), str(sequences[j].seq))
        distance_matrix[j, i] = distance_matrix[i, j]

# Print the distance matrix
print("Distance Matrix:")
print(distance_matrix)

# UPGMA clustering
constructor = DistanceTreeConstructor()
tree = constructor.upgma(_Matrix(list(range(num_sequences)), distance_matrix.tolist()))

# Print the resulting tree
print("\nUPGMA Tree:")
Phylo.draw_ascii(tree)
