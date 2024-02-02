'''
@author: olao
'''

class Sequence(object):     #
    '''
    classdocs
    '''
    def __init__(self, name, string_of_nucleotides,mutations=None):
        '''
        Constructor
        '''
        self.name = name    #make the name of the sequence available to all the following functions
        
        if isinstance(string_of_nucleotides, str):      #checks if the sequence given is  a string to avoid the class being used in the wrong way
            self.string_of_nucleotides = list(string_of_nucleotides)     #if the sequence is a string, make it into a list so as to be more available 
        elif isinstance(string_of_nucleotides,list):        #if it is not a string and is a list, maintain it that way
            self.string_of_nucleotides = string_of_nucleotides      #make the sequence available to 
        else:
            raise TypeError("Use a string to initialize the sequence or a list of nucleotides")     #if is is indeed not a string, raise and error and the computer crashes and the code stops running
            
            
        if mutations== None:        #the first sequence is not mutated, it is the ancestral 
            self.mutations = [0]*len(string_of_nucleotides) # create a list called mutations filled with 0 because there are none
        else:       #if it is not None then there are mutations
            self.mutations = mutations     #mutations is whatever it is    
    
    
    def nucleotide_at_position(self,position):      #find the nucleotide at given position
        return self.string_of_nucleotides[position]     #return directly the nucleotide from the sequence at that position
 
 
    def sequence_length(self):      #find the length of the sequence
        return len(self.mutations)      #return directly the length of the mutations 
    
    
    def get_name(self):     #obtain the name of the sequence currently using
        return self.name        #return the name 
   
    
    def copy(self, new_name):       #create a copy of the current sequence with the new given name 
        return Sequence(new_name,self.string_of_nucleotides.copy(),self.mutations.copy())       #call the function to create the copy
    
    
    def __str__(self):      #this will output the name of the sequence and the sequence itself as a string
        return self.name + ' : ' + str(self.string_of_nucleotides)      #design the output
    
    
    def mutate_nucleotide_at_position(self,position,nucleotide):        #create a given mutation at a given position  
        if(nucleotide!=self.string_of_nucleotides[position]):       #if the nucleotide is different to the one at the sequence's postions
            self.mutations[position] = self.mutations[position] + 1         #add one to the mutations at that given position
        
        self.string_of_nucleotides[position] = nucleotide       #if it is not different, then add the mutation  
        
        
    def get_number_of_mutations_at_each_position(self):     #find all the mutations 
        return self.mutations       #return the mutations containing the numbers of mutations at each positions


    
def main():         #run the code 
    
    sequence_a = Sequence("First_Species", list("ACTGACTG"))    #create a sequence needing a name and a string containing this sequence 
    sequence_b = sequence_a.copy("Second_Species")     #create a copy of the sequence to compare
    
    sequence_a.mutate_nucleotide_at_position(1, "C")        #create the mutations at the given positions and with the given nucleotide  in sequence a
    sequence_b.mutate_nucleotide_at_position(2, "A")        #create the mutations at the given positions and with the given nucleotide  in sequence b
    
    print(sequence_a)   #print the newly mutated sequence a
    print(sequence_b)   #print the newly mutated sequence b 
    print("") #print an empty line 
    
    print(sequence_a.get_number_of_mutations_at_each_position())    #print the number of mutations at each position of sequence a
    print(sequence_b.get_number_of_mutations_at_each_position())    #print the number of mutation s at each position of sequence b
    
    
if __name__ == "__main__":
    main () 
