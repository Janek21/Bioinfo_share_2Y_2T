'''
@author: Sergi Ocaña Alamo
'''

# Importing  classes from other files
from Sequence import Sequence
from Script_Alias import RandomMultinomial

#Define a class called Evolution 

class Evolution(object):
    '''
    Class representing an evolutionary process
    '''
    
    def __init__(self, ancestral_sequence, transition_matrix):
        '''
        Constructor to initialize the Evolution object
        '''
        # Checking if it is a Sequence object
        if not isinstance(ancestral_sequence, Sequence):
            # Raise an error if it is not a Sequence object
            raise TypeError("ancestral_sequence must be a Sequence object!")
        
        # Starting attributes
        # Dictionary to store evolving sequences with species names as keys
        self.evolving_sequences = {}
        
        # Adding the ancestral sequence to the evolving sequences dictionary
        self.evolving_sequences[ancestral_sequence.get_name()] = ancestral_sequence
        
        # Storing the transition matrix for nucleotide changes
        self.transition_matrix = transition_matrix
        
        # Dictionary to store RandomMultinomial objects for each nucleotide based on the transition matrix
        self.random_transition = {}

        # Creating a RandomMultinomial object for each nucleotide based on the transition matrix
        for key in self.transition_matrix:
            self.random_transition[key] = RandomMultinomial(list(transition_matrix[key].values()))
        
    #Define a function called get_sequence_species
    def get_sequence_species(self, name):

        # Get the Sequence object for a given species name
        return self.evolving_sequences[name]
    
    #Define a function called get_list_of_species
    def get_list_of_species_name(self):

        # Get a list of all species names in the evolving process
        return list(self.evolving_sequences.keys())
    
    
    def split_species_in_two(self, name_of_species_that_splits, new_name_of_species):
        
        # Create a copy of the specified species and add it to the evolving sequences with a new name
        new_sequence = self.evolving_sequences[name_of_species_that_splits].copy(new_name_of_species)
        self.evolving_sequences[new_sequence.get_name()] = new_sequence
    
    
    def evolve(self, generations):
    # Do evolution for the specified number of generations

        # Loop through each generation
        for gen in range(generations):

            # Loop through each species 
            for species in self.evolving_sequences:

                # Get the Sequence object for the current species
                sequence_species = self.evolving_sequences[species]

                # Loop through each position in the sequence
                for n in range(sequence_species.sequence_length()):

                    # Get the nucleotide at the current position in the sequence
                    nucleotide_at_position_n = sequence_species.nucleotide_at_position(n)

                    # Propose a change in the nucleotide based on random transition probabilities
                    propose_change = self.random_transition[nucleotide_at_position_n].sample()
                    # Get the nucleotide to change to based on the proposed change
                    nucleotide_propose_change = list(self.transition_matrix[nucleotide_at_position_n].keys())[propose_change]

                    # Print the original and proposed nucleotides for debugging or analysis
                    print(nucleotide_at_position_n, nucleotide_propose_change)

                    # Mutate the nucleotide at the current position in the sequence
                    sequence_species.mutate_nucleotide_at_position(n, nucleotide_propose_change)
              
    
def main():
    # Create an ancestral sequence with the name "Ancestral" and a string of nucleotides
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")

    # Define a transition matrix for nucleotide changes
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}

    # Create an Evolution object with the ancestral sequence and transition matrix
    evolution = Evolution(sequence_ancestral, transition_probability)
    
    # Split the ancestral species into two species with a new name
    evolution.split_species_in_two("Ancestral", "Species2")
    
    # Evolve the sequences for 1000 generations
    evolution.evolve(1000)
    
    # Print the final states of the Ancestral and Species2 sequences
    print(evolution.get_sequence_species("Ancestral"))
    print(evolution.get_sequence_species("Species2"))    

    
if __name__ == "__main__":
    main()
