
from Evolution import Evolution
from Sequence import Sequence

class ToolsToWorkWithSequence():

    def nucleotide_statistics(seq):
        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        length = seq.sequence_length()
        for position in range(length):
            nucleotide = seq.nucleotide_at_position(position)   
            counts[nucleotide] += 1
        for key in counts.keys():
            counts[key] = counts[key]/length
        return counts
    
    def observed_pairwaise_nucleotide(sequence1, sequence2):
        counter = 0
        seq1 = []
        seq2 = []
        length1= sequence1.sequence_length()
        for position in range(length1):
            seq1.append(sequence1.nucleotide_at_position(position))
        length2= sequence2.sequence_length()
        for position in range(length2):
            seq2.append(sequence2.nucleotide_at_position(position))
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                counter += 1
        return counter



def main():

    sequence = Sequence("First_Species", list("ACTGACTG"))
    freqs = ToolsToWorkWithSequence.nucleotide_statistics(sequence)
    for key in freqs.keys():
        print('For', key,', the frequency is', freqs[key])

    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}
    evolution = Evolution(sequence_ancestral, transition_probability)
    evolution.split_species_in_two("Ancestral", "Species2") 
    evolution.evolve(1000)
    seq1 = evolution.get_sequence_species("Ancestral")
    seq2 = evolution.get_sequence_species("Species2")
    print('There are ',ToolsToWorkWithSequence.observed_pairwaise_nucleotide(seq1, seq2), ' different nucleotides among sequences.')
    freq1 = ToolsToWorkWithSequence.nucleotide_statistics(seq1)
    print('For sequence A:')
    for key in freq1.keys():
        print('For', key,', the frequency is', freq1[key])
    freq2 = ToolsToWorkWithSequence.nucleotide_statistics(seq2)
    print('For sequence B:')
    for key in freq2.keys():
        print('For', key,', the frequency is', freq2[key])    


if __name__ == "__main__":
    main ()   