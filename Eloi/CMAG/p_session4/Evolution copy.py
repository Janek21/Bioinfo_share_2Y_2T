from Sequence import Sequence
from Alias_Vose import RandomMultinomial

class Evolution(object):
    # Class to represent an evolutionary process.
    
    def __init__(self, ancestral_sequence, transition_matrix):
        # Constructor for the Evolution class.
        
        # Check if the input ancestral_sequence is an instance of the Sequence class
        if not isinstance(ancestral_sequence, Sequence):
            raise TypeError("ancestral_sequence must be a Sequence object!")
        
        # Initialize evolving_sequences dictionary with the ancestral_sequence
        self.evolving_sequences = {ancestral_sequence.get_name(): ancestral_sequence}
        
        # Store the transition matrix and create a dictionary for random transitions
        self.transition_matrix = transition_matrix
        self.random_transition = {}
        
        # Populate the random_transition dictionary with RandomMultinomial instances
        for key in self.transition_matrix:
            self.random_transition[key] = RandomMultinomial(list(transition_matrix[key].values()))

    def get_sequence_species(self, name):
        # Get the sequence of a specific species by name.
        return self.evolving_sequences[name]
    
    def get_list_of_species_name(self):
        # Get a list of names of all species in the evolving process.
        return list(self.evolving_sequences.keys())
    
    def split_species_in_two(self, name_of_species_that_splits, new_name_of_species):
        # Split a species into two by creating a new sequence and adding it to the evolving process.
        new_sequence = self.evolving_sequences[name_of_species_that_splits].copy(new_name_of_species)
        self.evolving_sequences[new_sequence.get_name()] = new_sequence
    
    def evolve(self, generations):
        # Simulate evolution for a specified number of generations.
        for gen in range(generations):  # Loop through generations
            for species in self.evolving_sequences:  # Loop through species
                sequence_species = self.evolving_sequences[species]
                for n in range(sequence_species.sequence_length()):  # Loop through nucleotide positions
                    nucleotide_at_position_n = sequence_species.nucleotide_at_position(n)
                    
                    # Propose a change in the nucleotide based on the random transition probability
                    propose_change = self.random_transition[nucleotide_at_position_n].sample()
                    nucleotide_propose_change = list(self.transition_matrix[nucleotide_at_position_n].keys())[propose_change]
                    
                    # Mutate the nucleotide at the specified position
                    sequence_species.mutate_nucleotide_at_position(n, nucleotide_propose_change)

# Define main function
def main():
    # Create an ancestral sequence
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    
    # Define the transition probabilities for nucleotides
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88},
                              "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04},
                              "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04},
                              "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    
    # Initialize the Evolution class with the ancestral sequence and transition probabilities
    evolution = Evolution(sequence_ancestral, transition_probability)
    
    # Split the ancestral species into two species
    evolution.split_species_in_two("Ancestral", "Species2")
    
    # Simulate evolution for 1000 generations
    evolution.evolve(1000)
    
    # Print the final sequences of the ancestral and the new species
    print(evolution.get_sequence_species("Ancestral"))
    print(evolution.get_sequence_species("Species2"))    

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

