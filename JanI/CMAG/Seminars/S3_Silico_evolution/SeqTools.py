#!/usr/bin/python3

from Sequence import Sequence
from Evolution import  Evolution

class ToolsToWorkWithSequences(object):

    #constructor
    def __init__(self, seq):
        if not isinstance(seq, Sequence): #raise error if seq is not an object of class Sequence
            raise TypeError(">:/ seq must be a Sequence object")
        
        self.seq=seq #define seq so it can be used by all methods
    #############################################################################################################################################################################   
    #############################################################################################################################################################################
    ##How do I apply the method to each of the evolved sequences
    #############################################################################################################################################################################
    #############################################################################################################################################################################
    def nucleotide_statistics(self):

        nucl_count={"A":0, "C":0, "T":0, "G":0} #set up dictionary to count frequencies
        length=self.seq.sequence_length() #get sequence length

        for position in range(length): #iterate throught the length of the sequence to get the nucleotides
            nucleotide=self.seq.nucleotide_at_position(position) #get the nucleotide at each position
            nucl_count[nucleotide]+=1 #for each kind of nucleotide (A,C,T, G) add 1 to its count

        for nucleotide_key in nucl_count.keys(): #when you have counted all nucleotides iterate through the dictionary keys (ACTG)
            nucl_count[nucleotide_key]=nucl_count[nucleotide_key]/length #for each key update it to be its frequence (appearences/total)
        return nucl_count
    

    def observed_pairwise_nucleotide_distance(seq1, seq2):

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
            #print(nuc1, nuc2)
            if nuc1!=nuc2: #if they are different add 1 to the different nucleotides counter
                different_nuc+=1
        return different_nuc

    
def main():
    sequence_ancestral = Sequence("Ancestral", "ACTGACTGACTGACTGACTGACTGACTGACTGACTG")
    transition_probability = {"A":{"G":0.04,"C":0.04,"T":0.04,"A":0.88}, "C":{"G":0.04,"C":0.88,"T":0.04,"A":0.04}, "G":{"G":0.88,"C":0.04,"T":0.04,"A":0.04}, "T":{"G":0.04,"C":0.04,"T":0.88,"A":0.04}}

    evolution = Evolution(sequence_ancestral, transition_probability)

    evolution.split_species_in_two("Ancestral", "Species2")
    evolution.evolve(1000)

    species=evolution.get_list_of_species_name()
    
    for sp_name in species:
        species_sequence=evolution.get_sequence_species(sp_name)

        tool= ToolsToWorkWithSequences(species_sequence)

        print(f"For sequence {sp_name} the percentages are {tool.nucleotide_statistics()}")


    #tool= ToolsToWorkWithSequences()
    #tool.observed_pairwise_nucleotide_distance(species_sequence, last_seq)
    #print(tool.observed_pairwise_nucleotide_distance(sequence_a, sequence_b))

if __name__ == "__main__":
    main () 
