

class ToolsToWorkWithSeq(object):

    # Initializing the class
    def __init__(self):
        pass
    
    # Defining a function that will get the percentage of the nucleotides
    def nucleotide_statistics(self, seq):
        '''
        Calculate the percentage of A, C, T, G in a given sequence.

        Parameters:
        - seq: A sequence as a list of nucleotides.

        Returns:
            A dictionary with the percentage of each nucleotide.
        '''
        # length of the sequence
        s = len(seq)
        
        # Creating the dictionary that will have the count of each nucleotide
        nucleo = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

        # Iteration through each item of the variable seq (list or string)
        for x in seq:
            # Updating the count of the current nucleotide in the 'nucleo' dictionary
            nucleo[x] += (1 / s) * 100
        
        return nucleo  # Returning the result

    def observed_pairwise_nucleotide_distance(self, seq1, seq2):
        '''
        Calculate the number of nucleotides that, for the same position, are different in two sequences.

        Parameters:
        - seq1
        - seq2 
        Returns:
        The number of differing nucleotides at the same positions.
        '''
        # Checking which sequence is shorter to stop or not
        if len(seq2) > len(seq1):
            stop = len(seq1)
        else:
            stop = len(seq2)

        # Variable result
        result = 0

        # Loop to iterate through the longest sequence
        for x in range(stop):
            # If the nucleotides at the current position are different, add 1 to the result
            if seq1[x] != seq2[x]:
                result += 1

        # Taking into account the length difference
        result += abs(len(seq1) - len(seq2))

        return result  # Returning the output

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
    # Input
    seq = ['C', 'A', 'C', 'G', 'C', 'C', 'G', 'G', 'T', 'A', 'T', 'G', 'G', 'C', 'T', 'C', 'T', 'A', 'T', 'T', 'A', 'A', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'A', 'C', 'G', 'G', 'C', 'A', 'C']
    seq1 = ['C', 'A', 'C', 'G', 'C', 'C', 'G', 'G', 'T', 'A', 'T', 'G', 'G', 'C', 'T', 'C', 'T', 'A', 'T', 'T', 'A', 'A', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'A', 'C', 'G', 'G', 'C', 'A', 'C']
    seq2 = ['G', 'C', 'A', 'C', 'T', 'T', 'A', 'G', 'T', 'C', 'T', 'C', 'G', 'C', 'A', 'C', 'A', 'T', 'C', 'C', 'A', 'C', 'T', 'T', 'G', 'A', 'G', 'T', 'C', 'A', 'T', 'T', 'C', 'C', 'A', 'G']

    # Starting the class
    tools = ToolsToWorkWithSeq()

    # Calling the nucleotide_statistics function and printing the output
    stat = tools.nucleotide_statistics(seq)
    stat1 = tools.nucleotide_statistics(seq1)
    stat2 = tools.nucleotide_statistics(seq2)
    print(f'Nucleotide statistics for sequence: {stat}')

    print() 

    # Calling the observed_pairwise_nucleotide_distance function and printing the result
    pairwise = tools.observed_pairwise_nucleotide_distance(seq1, seq2)
    print(f'Number of different nucleotides: {pairwise}')
    print() 

if __name__ == "__main__":
    main()
