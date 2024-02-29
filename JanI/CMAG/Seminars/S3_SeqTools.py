#!/usr/bin/python3

from S3_Sequence import Sequence
from S3_Evolution import  Evolution

class ToolsToWorkWithSequences(object):

    #constructor
    def __init__(self, seq):
        if not isinstance(seq, Sequence): #raise error if seq is not an object of class Sequence
            raise TypeError(">:/ seq must be a Sequence object")
        
        self.seq=seq #define seq so it can be used by all methods
    
    def nucleotide_statistics(self):

        nucl_count={"A":0, "C":0, "T":0, "G":0} #set up dictionary to count frequencies
        length=self.seq.sequence_length() #get sequence length

        for position in range(length): #iterate throught the length of the sequence to get the nucleotides
            nucleotide=self.seq.nucleotide_at_position(position) #get the nucleotide at each position
            nucl_count[nucleotide]+=1 #for each kind of nucleotide (A,C,T, G) add 1 to its count

        for nucleotide_key in nucl_count.keys(): #when you have counted all nucleotides iterate through the dictionary keys (ACTG)
            nucl_count[nucleotide_key]=nucl_count[nucleotide_key]/length #for each key update it to be its frequence (appearences/total)
        return nucl_count
    

    def observed_pairwise_nucleotide_distance(self, seq1, seq2):

        length1=seq1.sequence_length() #get the length of the first sequence
        length2=seq2.sequence_length() #get the length of the second sequence

        #if the length are different, select a long and short
        if length2>length1: #if length of sequence 2 is longer than length of sequence 1
            short_length=length1 #define short length as length of sequence 1 and
            long_length=length2 #long length as length of sequence 2

        else: #in case that length of sequence 1 is longer than length of sequence 2, do as above, but inverse
            short_length=length2
            long_length=length1
        #this is so if a sequence is longer than the other all "missing" nucleotides counted as different in the 2 sequences
        #if they are the same length there wil be no difference for "extra" nucleotides, so different_nuc will be 0
        different_nuc=long_length-short_length
        
        for position in range(short_length): #we iterate over short length, because we only compare the ones that appear in both sequences, if there are extras they will already be accounted for
            nuc1=seq1.nucleotide_at_position(position) #define nuc1 as the nucleotide in the current position of seq1
            nuc2=seq2.nucleotide_at_position(position) #define nuc2 as the nucleotide in the current position of seq2

            if nuc1!=nuc2: #if they are different add 1 to the different nucleotides counter
                different_nuc+=1
        return different_nuc

    
def main():
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}

    evolution = Evolution(sequence_ancestral, transition_probability)

    #evolve 4 sequences
    evolution.split_species_in_two("Ancestral", "Ancestral1") #from Ancestral get the first generation sequence
    evolution.split_species_in_two("Ancestral", "Ancestral2") #from Ancestral get the second generation sequence
    evolution.evolve(100) #100 generations pass
    evolution.split_species_in_two("Ancestral1", "A1_G1_1") #at 100 generations from start ancestral 1 develops in 2 sequences (generation 1, sequences 1 and 2)
    evolution.split_species_in_two("Ancestral1", "A1_G1_2")
    evolution.evolve(50) #50 more generations pass
    evolution.split_species_in_two("Ancestral2", "A2_G1_1") ##at 150 generations from start ancestral 2 develops in 2 sequences (generation 1, sequences 1 and 2)
    evolution.split_species_in_two("Ancestral2", "A2_G1_2")
    evolution.evolve(150) #150 more generatins pass
    evolution.split_species_in_two("A1_G1_1", "SpeciesA") #at 100 and 150 generations from start, ancestral 1 and 2 have developed 2 sequences each, known as generation 1 
    evolution.split_species_in_two("A1_G1_2", "SpeciesB") #Now, 300 generations from start, each sequence from generation 1 has evolved into another sequence
    evolution.split_species_in_two("A2_G1_1", "SpeciesC")
    evolution.split_species_in_two("A2_G1_2", "SpeciesD")

    species=evolution.get_list_of_species_name() #get the name of all species and define species as that list
    
    for sp_name in species: #iterate throught the names of each evolved species

        if "Species" in sp_name: #only use the evolved sequences
            species_sequence=evolution.get_sequence_species(sp_name) #for each evolved species, get its sequence

            tool= ToolsToWorkWithSequences(species_sequence) #define the class using the sequence from the name we are currently on

            print(f"For sequence {sp_name} the percentages are {tool.nucleotide_statistics()}") #print the nucleotide frequencies of that sequence


    repetition=[] #create a list were to add all compared sequences, to avoid repeating a comparison
    for sp_name in species: #iterate throught the names of each evolved species

        if "Species" in sp_name: #only use the evolved sequences
            species_sequence=evolution.get_sequence_species(sp_name) #for each evolved sequence, get its species

            for against_sp_name in species: #iterate over the list again, to compare all species between each other

                if "Species" in against_sp_name and sp_name!=against_sp_name: #only use the names of the evolved sequences, and avoid comparing a sequence with itself
                    
                    if sorted(sp_name[-1]+against_sp_name[-1]) not in repetition: #to avoid repetition check if we have already compared the current species

                        other_species=evolution.get_sequence_species(against_sp_name) #get the sequence of the against species
                        
                        repetition.append(sorted(sp_name[-1]+against_sp_name[-1])) #add the current species in the repetition list to not repeat the later
                        
                        diff=tool.observed_pairwise_nucleotide_distance(species_sequence, other_species) #execute the function and observe for the current sequence against the another one of the evolved ones
                        
                        print(f"Between {sp_name[-1]} and {against_sp_name[-1]} there are {diff} different nucleotides")




if __name__ == "__main__":
    main () 
