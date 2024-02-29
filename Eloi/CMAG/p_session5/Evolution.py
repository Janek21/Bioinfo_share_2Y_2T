from Sequence import Sequence											# Import sequence class from sequence file
from Alias_Vose import RandomMultinomial								# Import randomMultinomial class from Alias_Vose

class Evolution(object):												# Class to represent an evolutionary process.
    
    def __init__(self, ancestral_sequence, transition_matrix):			# Constructor for the Evolution class.
        
        if not isinstance(ancestral_sequence, Sequence):				# Check if the input ancestral_sequence is an instance of the Sequence class
            raise TypeError("ancestral_sequence must be a Sequence object!")  #Raise Error
        
        self.evolving_sequences = {ancestral_sequence.get_name(): ancestral_sequence} # Initialize evolving_sequences dictionary with the ancestral_sequence
        
        self.transition_matrix = transition_matrix						# Store the transition matrix
        self.random_transition = {}										# Create a dictionary for random transitions
        
        for key in self.transition_matrix:								# Iterate over each key in the transition matrix
            self.random_transition[key] = RandomMultinomial(list(transition_matrix[key].values())) # Populate the random_transition dictionary with RandomMultinomial instances

    def get_sequence_species(self, name):								# Define the function to get the sequence species with name as an argument
        return self.evolving_sequences[name] 							# Get the sequence of a specific species by name.
    
    def get_list_of_species_name(self): 								# Define the function to get a list of names of all species in the evolving process.
        return list(self.evolving_sequences.keys())						# return the kys of the evolving sequences dictionnary
    
    def split_species_in_two(self, name_of_species_that_splits, new_name_of_species): # Define a function to split a species into two by creating a new sequence and adding it to the evolving process.
        new_sequence = self.evolving_sequences[name_of_species_that_splits].copy(new_name_of_species) # Retrieve the existing sequence that will split into two
        self.evolving_sequences[new_sequence.get_name()] = new_sequence # Create a new sequence by copying the existing sequence with a new name
    
    def evolve(self, generations):										# Define function to simulate evolution for a specified number of generations. 
        for gen in range(generations):  								# Loop through generations
            for species in self.evolving_sequences:  					# Loop through species
                sequence_species = self.evolving_sequences[species]		# Retrieve the sequence of the current species from the evolving_sequences dictionary
                for n in range(sequence_species.sequence_length()):  	# Loop through nucleotide positions in the sequence of the current species
                    nucleotide_at_position_n = sequence_species.nucleotide_at_position(n) # Get the nucleotide at the current position in the sequence
                    
                    propose_change = self.random_transition[nucleotide_at_position_n].sample() # Propose a change in the nucleotide based on the random transition probability
                    nucleotide_propose_change = list(self.transition_matrix[nucleotide_at_position_n].keys())[propose_change] # Determine the new nucleotide based on the proposed change
                    
                    sequence_species.mutate_nucleotide_at_position(n, nucleotide_propose_change) # Mutate the nucleotide at the specified position

def main():																# Define main function
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG") # Create an ancestral sequence
    
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88},
                              "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04},
                              "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04},
                              "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}# Define the transition probabilities for nucleotides
    
    evolution = Evolution(sequence_ancestral, transition_probability) 	# Initialize the Evolution class with the ancestral sequence and transition probabilities
    
    evolution.split_species_in_two("Ancestral", "Species2")				# Split the ancestral species into two species
			
    evolution.evolve(1000)												# Simulate evolution for 1000 generations
    
    print(evolution.get_sequence_species("Ancestral"))					# Print the final sequences of the ancestral
    print(evolution.get_sequence_species("Species2"))    				# Print the final sequences of the new species

if __name__ == "__main__": 												# Execute the main function if the script is run directly
    main()

