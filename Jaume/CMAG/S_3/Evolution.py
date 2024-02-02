'''
@author: Jaume Jurado Sánchez
NIA: 107682
'''

from Sequence import Sequence
from Alias_Vose_already_comented import RandomMultinomial

class Evolution(object):
    '''
    classdocs
    '''
    
    def __init__(self, ancestral_sequence, transition_matrix):
        '''
        Constructor
        '''
        # Checking the type of input we have
        if not isinstance(ancestral_sequence, Sequence):

            # If it is not the correct one it raises an error
            raise TypeError("ancestral_sequence must be a Sequence object!")
        
        self.evolving_sequences = {}
        self.evolving_sequences[ancestral_sequence.get_name()] = ancestral_sequence
        self.transition_matrix = transition_matrix
        self.random_transition = {}

        for key in self.transition_matrix:
            self.random_transition[key] = RandomMultinomial(list(transition_matrix[key].values()))
        
    
    def get_sequence_species(self,name):
        return self.evolving_sequences[name]
    
    
    def get_list_of_species_name(self):
        return list(self.evolving_sequences.keys())
    
    
    def split_species_in_two(self,name_of_species_that_splits, new_name_of_species):
        new_sequence = self.evolving_sequences[name_of_species_that_splits].copy(new_name_of_species)
        self.evolving_sequences[new_sequence.get_name()] = new_sequence
    
    
    def evolve(self, generations):

        for gen in range(generations):

            for species in self.evolving_sequences:

                sequence_species = self.evolving_sequences[species]

                for n in range(sequence_species.sequence_length()):

                    nucleotide_at_position_n = sequence_species.nucleotide_at_position(n)
                    propose_change = self.random_transition[nucleotide_at_position_n].sample()
                    nucleotide_propose_change = list(self.transition_matrix[nucleotide_at_position_n].keys())[propose_change]
                    print(nucleotide_at_position_n,nucleotide_propose_change)
                    sequence_species.mutate_nucleotide_at_position(n,nucleotide_propose_change)               
    
def main():

    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)
    
    evolution.split_species_in_two("Ancestral", "Species2")
    
    evolution.evolve(1000)
    
    print(evolution.get_sequence_species("Ancestral"))
    print(evolution.get_sequence_species("Species2"))    

    
if __name__ == "__main__":
    main ()