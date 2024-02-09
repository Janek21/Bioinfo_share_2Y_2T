'''
@author: olao
'''
from Sequence import Sequence
from AliasVose import RandomMultinomial

class Evolution(object): # create a class called evolution.
    '''
    classdocs
    '''
    def __init__(self, ancestral_sequence, transition_matrix): # define the init function, that will take as argument selt, an ancestral sequence and a transition matrix.
        '''
        Constructor
        '''
        if not isinstance(ancestral_sequence, Sequence): # if the ancestral sequence is not a sequence.
            raise TypeError("ancestral_sequence must be a Sequence object!") # raise an error.
        
        self.evolving_sequences = {} # define self.evolving_sequences as an empty dictionary
        # get the name of an ancestral sequence and store it in a dictionary, having as a value its ancestral sequence.
        self.evolving_sequences[ancestral_sequence.get_name()] = ancestral_sequence 
        self.transition_matrix = transition_matrix # store in self.transition_matrix the variable transition matrix.
        self.random_transition = {} # define self.random_transition as an empty dictionary.
        for key in self.transition_matrix: # iterate over self.transition_matrix.
            # assign to each key a random value (from the random multiomial).
            self.random_transition[key] = RandomMultinomial(list(transition_matrix[key].values()))
        
    
    def get_sequence_species(self,name): # define a function that takes as a argument self and name.
        return self.evolving_sequences[name] # returns the sequence of the given name.
    
    
    def get_list_of_species_name(self): # define a funcion that takes as argument self. 
        return list(self.evolving_sequences.keys()) # return a list with all the names of the species.
    
    # define a function that takes as argument self, name_of_species_that_splits and new_name_of_species.
    def split_species_in_two(self,name_of_species_that_splits, new_name_of_species):
        # new_sequence is a copy of the sequence coming from the specie that splits.
        new_sequence = self.evolving_sequences[name_of_species_that_splits].copy(new_name_of_species)
        # add the new_sequence name as a new entry in the dictionary. It's value will be the new sequence.
        self.evolving_sequences[new_sequence.get_name()] = new_sequence
    
    
    def evolve(self, generations): # define a function evolve that takes as arguments self and generations.
        for gen in range(generations): # iterate over the generations.
            for species in self.evolving_sequences: # iterate over evolving_sequences.
                sequence_species = self.evolving_sequences[species] # get the sequence of each species.
                for n in range(sequence_species.sequence_length()): # iterate over the length of the sequence.
                    # get the nucleotide at each position
                    nucleotide_at_position_n = sequence_species.nucleotide_at_position(n)
                    # get a random change from the random transition dictionary taking as key the nucleotide at each position.
                    propose_change = self.random_transition[nucleotide_at_position_n].sample()
                    # get the nucleotide that has been mutated.
                    nucleotide_propose_change = list(self.transition_matrix[nucleotide_at_position_n].keys())[propose_change]
                    #print(nucleotide_at_position_n,nucleotide_propose_change)
                    # mutate the ancestral nucelotide by the new one (nucleotide_purpose_change).
                    sequence_species.mutate_nucleotide_at_position(n,nucleotide_propose_change)               

            
def main():
    # define the ancestral sequence.
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    # define the transition probability matrix.
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    # create the Evolution object.
    evolution = Evolution(sequence_ancestral, transition_probability)
    
    # implementation of the schema
    evolution.split_species_in_two("Ancestral", "A1") # get A1 from the ancestral sequence
    evolution.split_species_in_two("Ancestral", "A2") # get A2 from the ancestral sequence
    evolution.evolve(100) # 100 generations after
    evolution.split_species_in_two("A1", "A1_100_A") # get A1_100_A form A1
    evolution.split_species_in_two("A1", "A1_100_B") # get A1_100_B form A1
    evolution.evolve(50)
    evolution.split_species_in_two("A2", "A2_150_A") # get A2_150_A form A2
    evolution.split_species_in_two("A2", "A2_150_B") # get A2_150_B form A2
    evolution.evolve(150)
    evolution.split_species_in_two("A1_100_A", "SpeciesA") # get SpeciesA from A1_100_A
    evolution.split_species_in_two("A1_100_B", "SpeciesB") # get SpeciesB from A1_100_B
    evolution.split_species_in_two("A2_150_A", "SpeciesC") # get SpeciesC from A2_150_A
    evolution.split_species_in_two("A2_150_B", "SpeciesD") # get SpeciesD from A2_150_B

    # get the sequence of each species.
    print(evolution.get_sequence_species("SpeciesA"))
    print(evolution.get_sequence_species("SpeciesB"))
    print(evolution.get_sequence_species("SpeciesA"))
    print(evolution.get_sequence_species("SpeciesB"))

    
if __name__ == "__main__":
    main ()         
        
        