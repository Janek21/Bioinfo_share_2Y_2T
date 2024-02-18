from Sequence import Sequence
from Evolution import Evolution
from ToolsToWorkWithSequencesfinal import ToolsToWorkWithSequence
from DistanceMatrix import DistanceMatrix

import copy

class DistanceBasedAlgorithms(object):

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    
    def upgma(self):
 
        distance_matrix = self.distance_matrix
        # Initialize variables
        while distance_matrix.n_rows() >1 :
            min_d = distance_matrix.get_value_i_j(0,1)
            min_i = 0
            min_j = 1
            for i in range(distance_matrix.n_rows()-1):
                for j in range(i+1, distance_matrix.n_rows()):
                    if distance_matrix.get_value_i_j(i,j) < min_d:
                        min_d = distance_matrix.get_value_i_j(i,j)
                        min_i = i
                        min_j = j
            
            species_names = distance_matrix.get_name_of_species()
            newname = "(" + species_names[0] + ":" + str(min_d/2) + ', ' + species_names[min_j] + ":" + str(min_d/2) + ")"
            distance_matrix.change_name_species_i(min_i, newname)
            for x in range(distance_matrix.n_rows()):
                if x != min_i and x != min_j:
                    d_i = distance_matrix.get_value_i_j(min_i, x)
                    d_j = distance_matrix.get_value_i_j(min_j, x)
                    new_distance = (d_i+d_j)/2
                    distance_matrix.add_value_i_j(min_i, x, new_distance)
            distance_matrix.remove_species_i(min_j)
        return species_names[0]







def main():        
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)
    seqA = sequence_ancestral.copy('Seq_A')
    evolution.evolve(1000)
    seqB = sequence_ancestral.copy('Seq_B')
    evolution.evolve(1000)
    seqC = sequence_ancestral.copy('Seq_C')
    evolution.evolve(1000)
    seqD = sequence_ancestral.copy('Seq_D')

    distance_matrix = DistanceMatrix(['SeqA', 'SeqB', 'SeqC', 'SeqD'])
    list_of_seqs = [seqA, seqB, seqC, seqD]
    for i in range(len(distance_matrix.get_name_of_species())):
        for j in range(len(distance_matrix.get_name_of_species())):
            d = ToolsToWorkWithSequence.observed_pairwise_nucleotide_distance(list_of_seqs[i],list_of_seqs[j])
            distance_matrix.add_value_i_j(i,j,d)
    matrix = DistanceBasedAlgorithms(distance_matrix)
    # Print the distance matrix
    print("Distance Matrix:")
    for i in range(distance_matrix.n_rows()):
        for j in range(distance_matrix.n_rows()):
            print(distance_matrix.get_value_i_j(i, j), end=" ")
        print() 

    sol = matrix.upgma()
    print(sol)



if __name__ == "__main__":
    main ()         
    

		
