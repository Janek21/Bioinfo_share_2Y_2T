'''

@author: olao
'''
from Sequence import Sequence
from Probability_simulation import RandomMultinomial

class Evolution(object):
    '''
    classdocs
    '''
    
    def __init__(self, ancestral_sequence, transition_matrix):
        '''
        Constructor
        '''
        if not isinstance(ancestral_sequence, Sequence): #if ancestral_sequence is not of type object (Sequence), raise the Error
            raise TypeError("ancestral_sequence must be a Sequence object!")
        
        self.evolving_sequences = {}
        self.evolving_sequences[ancestral_sequence.get_name()] = ancestral_sequence #use get_name() function of class Sequence to assign the name of the sequence as key and the Sequence object as value in the dictionary evolving_sequences
        self.transition_matrix = transition_matrix #make it so all methods can access transition_matrix
        self.random_transition = {}
        for key in self.transition_matrix: #for each key in transition_matrix randomize its values list, and reassign it to the same key
            self.random_transition[key] = RandomMultinomial(list(transition_matrix[key].values()))
        
    
    def get_sequence_species(self,name): #if this method is called return the sequence for that name (use the name as key in evolving_sequences)
        return self.evolving_sequences[name]
    
    
    def get_list_of_species_name(self): #prints the names of all sequences as a list
        return list(self.evolving_sequences.keys())
    
    
    def split_species_in_two(self,name_of_species_that_splits, new_name_of_species): #given the name of the species that is going to split and the name of the new species
        new_sequence = self.evolving_sequences[name_of_species_that_splits].copy(new_name_of_species) #create a variable new_sequence that is a Sequence object copy of the species that splits using new_name_of_species as name
        self.evolving_sequences[new_sequence.get_name()] = new_sequence #define an entry into the evolving_sequences dictionary with the new sequence name as key and the new_sequence Sequence object as value
    
    
    def evolve(self, generations):
        for gen in range(generations): #iterate over the number of generations to repeat the code in the for loop x times (the code will be "repeated" 1000 times if we don't change the parameters in main())
            for species in self.evolving_sequences: #iterate over the keys(names) of the species in evolving_sequences
                sequence_species = self.evolving_sequences[species] #for each species (name of a specie in evolving_sequences) get its sequence in the variable sequence_species
                for n in range(sequence_species.sequence_length()): #iterate over the length of the just defined sequence, with the position being n
                    nucleotide_at_position_n = sequence_species.nucleotide_at_position(n) #get the nucleotide at position n
                    print(nucleotide_at_position_n)
                    propose_change = self.random_transition[nucleotide_at_position_n].sample() ##get a random position of the random transition numbers for the nucleotide that we are currently iterating over  (the one that corresponds to this base used as key in random_transition)
                    nucleotide_propose_change = list(self.transition_matrix[nucleotide_at_position_n].keys())[propose_change] ##using the current nucleotide as a key, get the next nucleotide using the variable defined above as a position inside the nested dictionary
                    #print(nucleotide_at_position_n,nucleotide_propose_change)
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
        
        