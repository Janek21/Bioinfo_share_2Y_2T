from Evolution import Evolution
from Sequence import Sequence
from DistanceMatrix import DistanceMatrix
from SeqTools import ToolsToWorkWithSequences

class DistanceBasedAlgorithms(object):
    '''
    classdocs
    '''

    def __init__(self, d_matrix): #d_matrix already contains the distances between sequences
        '''
        Constructor
        '''
        self.d_matrix = d_matrix #define d_matrix so that it can be used by any method
    
    def UPGMA(self):
        umatrix = self.d_matrix.copy() #we get a copy of the matrix to avoid editing the original one

        while umatrix.n_rows()>1: #this loops until the matrix has only 1 row left

            length=umatrix.n_rows() #define length as the number of rows in the matrix
            min_val=umatrix.get_value_i_j(0,1) #set minimum value as the value in first row second corner
            min_pos=[0, 1] #minimum position for i and j [i, j]

            for i in range(length): #iterate thorugh row positions
                for j in range(i+1, length): #the matrix is square, so this iterates through column positions

                    if umatrix.get_value_i_j(i, j) < min_val: #if current is < than minimum
                        min_val=umatrix.get_value_i_j(i, j) #make current minimum
                        min_pos[0]=i #and store the position of the current minimum in a list (for row)
                        min_pos[1]=j #(for column)

            species_names=umatrix.get_name_of_species() #store all names of species present in the matrix

            new_name=f"({species_names[min_pos[0]]}:{min_val/2}, {species_names[min_pos[1]]}:{min_val/2})" #create new name of species by getting the species in the row position of the smallest value in the matrix+ the halved minimum value, 
            #and getting the species name in the column position of the smallest value in the matrix+ the halved minimum value

            umatrix.change_name_species_i(min_pos[0], new_name) #changes name of species in minimum i position to the created name
            
            for x in range(length): #iterate through the length of the matrix

                if x!=min_pos[0] and x!=min_pos[1]: #if the number of the iteration is different than the position(in rows or columns) of minimum value of the matrix

                    i=umatrix.get_value_i_j(min_pos[0], x) #define i as the value in the same row of the minimum value and column of the current iteration
                    j=umatrix.get_value_i_j(min_pos[1], x) #define j as the value in the row (the row has the position number of column of the minimum value) and column of the current iteration
                    c_distance=(i+j)/2 #calculate c_distance to be the the sum of the 2 values mentioned above divided by 2
                    
                    umatrix.add_value_i_j(min_pos[0], x, c_distance) #add the calculated distance in the same row of the minimum value and in the column we are iterating over

            umatrix.remove_species_i(min_pos[1]) #remove species in the position of the column of the minimum value

        return species_names[0]


def main():
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)

    #evolve 4 sequences
    evolution.split_species_in_two("Ancestral", "Ancestral1") #from Ancestral get the first generation sequence
    evolution.split_species_in_two("Ancestral", "Ancestral2") #from Ancestral get the second generation sequence
    evolution.evolve(100) #100 generations pass
    evolution.split_species_in_two("Ancestral1", "A1_G1_1") #at 100 generations from start ancestral 1 develops in 2 sequences (generation 1, sequences 1 and 2)
    evolution.split_species_in_two("Ancestral1", "A1_G1_2")
    evolution.evolve(50) #50 more generations pass
    evolution.split_species_in_two("Ancestral2", "A2_G1_1") ##at 150 generations from start ancestral 2 develops in 2 sequences (generation 1, sequences 1 and 2)
    evolution.split_species_in_two("Ancestral2", "A2_G1_2")
    evolution.evolve(150) #150 more generatins pass
    evolution.split_species_in_two("A1_G1_1", "A") #at 100 and 150 generations from start, ancestral 1 and 2 have developed 2 sequences each, known as generation 1 
    evolution.split_species_in_two("A1_G1_2", "B") #Now, 300 generations from start, each sequence from generation 1 has evolved into another sequence
    evolution.split_species_in_two("A2_G1_1", "C")
    evolution.split_species_in_two("A2_G1_2", "D")

    species_names=evolution.get_list_of_species_name() #get the name of all species and define species as that list
    species_names=species_names[-4:] #get the names of only the last 4 sequences (the "last" descendants)

    seq=[] #define a empty list to gather the sequences
    for name in species_names: #iterate over the sequence names (the completely evolved)
        seq.append(evolution.get_sequence_species(name)) #for each name in the list get its corresponding sequence

    dist_mat=DistanceMatrix(species_names)#use the list of names of species as input for the DistanceMatrix class

    for sp1 in range(len(species_names)): #iterate over the positions of species names
        tool=ToolsToWorkWithSequences(seq[sp1]) #define the class ToolsToWorkWithSequences using the sequence correspondent to the name defined by the iteration

        for sp2 in range(len(species_names)): #iterate over the postions of species names again, to compare all species
            distance=tool.observed_pairwise_nucleotide_distance(seq[sp1], seq[sp2]) #compare the sequence defined by the first loop with the sequence defined by the second loop
            dist_mat.add_value_i_j(sp1, sp2, distance) #define each position in dist_mat as the distance between the nucleotides in the corresponding (row and column) sequences
    
    for row in dist_mat.m: #print the resulting distance matrix
        print(row)

    dba = DistanceBasedAlgorithms(dist_mat) #define dba as the DistanceBasedAlgorithms class with the distance matrix as object
    sol=dba.UPGMA() #calculate the UPGMA for dist_mat
    print("UPGMA")
    print(sol) #print the solution
    

if __name__ == "__main__":
    main ()
