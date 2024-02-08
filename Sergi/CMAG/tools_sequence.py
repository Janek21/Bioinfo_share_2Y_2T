
from Evolution import Evolution
from Sequence import Sequence

class ToolsToWorkWithSeq(object):

    # Initializing the class
    def __init__(self):
        pass
    
    # Defining a function that will get the percentage of the nucleotides
    def nucleotide_statistics(seq):
        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        length = seq.sequence_length()
        for position in range(length):
            nucleotide = seq.nucleotide_at_position(position)   
            counts[nucleotide] += 1
        for key in counts.keys():
            counts[key] = counts[key]/length
        return counts
    

    @staticmethod
    def observed_pairwise_nucleotide_distance(sequence_a, sequence_b):
        result = [1 if sequence_a.nucleotide_at_position(pos) != sequence_b.nucleotide_at_position(pos) else 0 for pos in range(sequence_a.sequence_length())]
        return sum(result)

    # Additional method as requested in the previous task
    def apply_methods_to_evolved_sequences(self, evolution_object):
        '''
        Apply nucleotide_statistics and observed_pairwise_nucleotide_distance methods to each evolved sequence.

        Parameters:
        - evolution_object: An Evolution object containing evolved sequences.
        '''
        # Iterate through each species in the evolving sequences
        for species_name in evolution_object.get_list_of_species_name():
            # Get the sequence object for the current species
            species_sequence = evolution_object.get_sequence_species(species_name)
            
            # Apply nucleotide_statistics to the sequence
            nucleotide_nucleo = self.nucleotide_statistics(species_sequence.string_of_nucleotides)
            print(f"Nucleotide statistics for {species_name}: {nucleotide_nucleo}")

            # Apply observed_pairwise_nucleotide_distance to the sequence and the ancestral sequence
            pairwise_distance = self.observed_pairwise_nucleotide_distance(
                species_sequence.string_of_nucleotides,
                evolution_object.get_sequence_species("Ancestral").string_of_nucleotides
            )
            print(f"Observed pairwise nucleotide distance between {species_name} and Ancestral: {pairwise_distance}")
            print()  

def main():

    sequence = Sequence("First_Species", list("ACTGACTG"))
    freqs = ToolsToWorkWithSeq.nucleotide_statistics(sequence)
    for key in freqs.keys():
        print('For', key,', the frequency is', freqs[key])

    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)
    evolution.split_species_in_two("Ancestral", "Species2") 
    evolution.evolve(1000)
    seq1 = evolution.get_sequence_species("Ancestral")
    seq2 = evolution.get_sequence_species("Species2")
    print('There are ',ToolsToWorkWithSeq.observed_pairwise_nucleotide_distance(seq1, seq2), ' different nucleotides among sequences.')
    freq1 = ToolsToWorkWithSeq.nucleotide_statistics(seq1)
    print('For sequence A:')
    for key in freq1.keys():
        print('For', key,', the frequency is', freq1[key])
    freq2 = ToolsToWorkWithSeq.nucleotide_statistics(seq2)
    print('For sequence B:')
    for key in freq2.keys():
        print('For', key,', the frequency is', freq2[key])    


if __name__ == "__main__":
    main ()   

if __name__ == "__main__":
    main()
