from Evolution import Evolution
from HiddenMarkovModel_To_Students import HiddenMarkovModel
from Sequence import Sequence
class ToolsToWorkWithSequences(object):

	def nucleotide_statistics(self, sequence):
		total_length = len(sequence)
		a_percentage = sequence.count("A") / total_length * 100
		c_percentage = sequence.count("C") / total_length * 100
		t_percentage = sequence.count("T") / total_length * 100
		g_percentage = sequence.count("G") / total_length * 100
		
		return {"A": a_percentage, "C": c_percentage, "T": t_percentage, "G": g_percentage}

	def observed_pairwise_nucleotide_distance(self, sequence_a, sequence_b):
		result = [1 if sequence_a.nucleotide_at_position(pos) != sequence_b.nucleotide_at_position(pos) else 0 for pos in range(sequence_a.sequence_length())]
		return float(sum(result))


def main():
	
	'''
	Generate Sequence
	'''
	tools = ToolsToWorkWithSequences()
	transition_probability = {"S":{"S":0.9,"L":0.1},"L":{"S":0.2,"L":0.8}};
	emission_probability = {"S":{"G":0.1,"C":0.2,"T":0.2,"A":0.5}, "L":{"G":0.01,"C":0.1,"T":0.3,"A":0.59}}
	hmm = HiddenMarkovModel(transition_probability, emission_probability)
	seq1 = hmm.generate_sequence(20, {"S":0.5, "L":0.5})
	seq_str = ''.join(seq1[0])
	
	'''
	Evolve sequence
	'''
	sequence_ancestral = Sequence("Ancestral", seq_str)
	
	# Define the transition probabilities for nucleotides
	transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88},
							  "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04},
							  "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04},
							  "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
	
	# Initialize the Evolution class with the ancestral sequence and transition probabilities
	evolution = Evolution(sequence_ancestral, transition_probability)
	
	# Split the ancestral species into two species
	evolution.split_species_in_two("Ancestral", "Species2")
	
	for times in range(100):
		evolution.evolve(1)
		seq1= evolution.get_sequence_species("Ancestral")
		seq2= evolution.get_sequence_species("Species2")
		j = tools.nucleotide_statistics(seq1)
		i = tools.observed_pairwise_nucleotide_distance(seq1,seq2)
	



if __name__ == "__main__":
	main()
