'''
@author: Laia Barcenilla, 107694
'''

from Sequence import Sequence
from Evolution import Evolution

# Define a class that will contain our functions.
class ToolsToWorkWithSequences(object):
    '''
    Constructor
    '''
    def __init__(self, seq): # define the init function that takes as argument self and seq (a sequence).
        if not isinstance(seq, Sequence): # if the seq is not a sequence.
            raise TypeError('The ancestral sequence must be a Sequence object') # raise an error.

        self.seq = seq # define self.seq as seq.

    # define a function that takes as argument self.
    def nucleotide_statistics(self):
        nucl2freq = {} # create an empty dictionary.
        length = self.seq.sequence_length() # get the length of the sequence.
        for position in range(length): # iterate over the sequence length.
            nucleotide = self.seq.nucleotide_at_position(position) # get the nucleotide at the position.
            if nucleotide not in nucl2freq: # if the nucleotide is not in the dictionary.
                # store as value 1 divided by the length (to have a frequency) and multiplyed by 100 (to have it as a percentage).
                nucl2freq[nucleotide] = 1/length * 100 
            else: # otherwise
                nucl2freq[nucleotide] += 1/length * 100 # add 1 to the entry.
        return nucl2freq # return the dictionary.

    # define a function that takes as argument self and mutated_sequence.
    def observed_pairwise_nucleotide_distance(self, mutated_sequence):
        if not isinstance(mutated_sequence, Sequence): # if the mutated sequence is not a sequence.
            raise TypeError('The mutated sequence must be a Sequence object') # raise an error.

        count = 0 # define the counter at 0.
        length = self.seq.sequence_length() # get the sequence length.
        for position in range(length): # iterate over the length of the sequence.
            nucleotide_A = self.seq.nucleotide_at_position(position) # get the nucleotide at the position in the ancestral sequence.
            nucleotide_B = mutated_sequence.nucleotide_at_position(position) # get the nucleotide at the position in the mutated sequence.

            if nucleotide_A != nucleotide_B: # if the nucleotides are different.
                count += 1 # add 1 to the count.
        return count # return the count (number of times that the nucleotides were diferent).


def main():
    # define the ancestral sequence.
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    # define the transition probability matrix.
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    
    # create the Evolution object.
    evolution = Evolution(sequence_ancestral, transition_probability)
    # create the ToolsToWorkWithSequences object.
    tools = ToolsToWorkWithSequences(sequence_ancestral)

    evolution.split_species_in_two('Ancestral', 'A1') # split the species in 2.
    evolution.evolve(100) # Evolve 100 generations.

    seq2 = evolution.get_sequence_species('A1') # get the sequence of specie A1.
    # Print the distance between the Ancestral and A1.
    print(f'The distance between sequences is: {tools.observed_pairwise_nucleotide_distance(seq2)}')

    frequency = tools.nucleotide_statistics() # get the dictionary that nucleotide_statistics returns as frequency.
    for freq in frequency: # iterate over the keys of the dictionary.
        print(f'The frequency for {freq} is {frequency[freq]}') # output the keys and the values.
    

if __name__ == '__main__':
    main()