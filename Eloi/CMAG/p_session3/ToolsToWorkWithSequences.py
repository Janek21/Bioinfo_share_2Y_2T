from Evolution import Evolution											# Import Evolution class
from HiddenMarkovModel_To_Students import HiddenMarkovModel				# Import HiddenMarkovModel class
from Sequence import Sequence											# Import Sequence class

class ToolsToWorkWithSequences(object):
	
	def nucleotide_statistics(self, sequence):							 # Calculate the percentage of each nucleotide in the sequence
		total_length = sequence.sequence_length()
		
		sequence_str = sequence.string_of_nucleotides					# Convert sequence to str to count nucleotides efficiently
		
		a_percentage = sequence_str.count("A") / total_length * 100		# Generate percentage of A
		c_percentage = sequence_str.count("C") / total_length * 100		# Generate percentage of C
		t_percentage = sequence_str.count("T") / total_length * 100		# Generate percentage of T
		g_percentage = sequence_str.count("G") / total_length * 100		# Generate percentage of G
		
		return {"A": a_percentage, "C": c_percentage, "T": t_percentage, "G": g_percentage} # Return all percentages

	def observed_pairwise_nucleotide_distance(self, sequence_a, sequence_b): # Calculate the observed pairwise nucleotide distance between two sequences
		result = [1 if sequence_a.nucleotide_at_position(pos) != sequence_b.nucleotide_at_position(pos) else 0 for pos in range(sequence_a.sequence_length())] # Create a list comprehension to compare nucleotides at each position of two sequences (sequence_a and sequence_b)
		return sum(result) # Sum the values in the result list, counting the number of differing nucleotides between the two sequences

def main():
    
    #Generate Sequence  
    tools = ToolsToWorkWithSequences()									# Initialize a toolset for working with sequences
    transition_probability = {"S":{"S":0.9,"L":0.1},"L":{"S":0.2,"L":0.8}} # Define transition probabilities for a Hidden Markov Model
    emission_probability = {"S":{"G":0.1,"C":0.2,"T":0.2,"A":0.5}, "L":{"G":0.01,"C":0.1,"T":0.3,"A":0.59}}# Define emission probabilities for a Hidden Markov Model
    hmm = HiddenMarkovModel(transition_probability, emission_probability)# Create a Hidden Markov Model instance
    seq1 = hmm.generate_sequence(20, {"S":0.5, "L":0.5})				# Generate a sequence of length 20 using the HMM with initial state probabilities
    seq_str = ''.join(seq1[0])											# Join sequence list into string
    print(seq_str)  													# Print the generated sequence string
       
    #Evolve sequence
    sequence_ancestral = Sequence("Ancestral", seq_str)					# Create an ancestral sequence instance
																		# Define transition probabilities for nucleotides in the Evolution class
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88},
                              "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04},
                              "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04},
                              "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)	# Initialize the Evolution class with the ancestral sequence and transition probabilities
    evolution.split_species_in_two("Ancestral", "Species2")
        
    for times in range(100):											# Evolve the sequences for 100 iterations
        evolution.evolve(1)
        seq1 = evolution.get_sequence_species("Ancestral")				# Get sequence 1
        seq2 = evolution.get_sequence_species("Species2")				# Get sequence 2
        
        j = tools.nucleotide_statistics(seq1)							# Calculate nucleotide statistics for the evolved sequence
        i = tools.observed_pairwise_nucleotide_distance(seq1, seq2)		# Calculate observed pairwise nucleotide distance between the two species
 
        print(j)  														# Print nucleotide percentages
        print(f'{i}\n')  												# Print pairwise distance

	



if __name__ == "__main__":
	main()
