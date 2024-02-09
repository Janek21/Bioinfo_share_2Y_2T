'''
@author: olao
'''

class Sequence(object): # define a class named Sequence.
    '''
    classdocs
    '''

    def __init__(self, name, string_of_nucleotides, mutations=None): # define the init funcition that takes as arguments name, a string of nucleotides and mutations.
        '''
        Constructor

        Why are we using list(str)? 
        We are thansforming the string_of_nucleotides into a list because we want to have each nucleotide stored individually in order to be able to mutate it.
        It is not possible to chane an element inside a string acessing by index. However, in a list it is.
        In this exercise, it is important to do it since we are mutating a sequence, so without transforming it into a list, we wouldn't be able to change the nucleotides.

        What is this mutations=None doing?
        When defining the __init__ function, we define mutations as None.
        Doing this, we are setting, by default, that our sequence doesn't contain any mutation (no argument needed to be given).
        In the case that our sequence contained mutations, we will store them directly into self.mutations.
        '''

        self.name = name # define self.name as name
    
        if isinstance(string_of_nucleotides, str): # if string_of_nucleotides is a string.
            self.string_of_nucleotides = list(string_of_nucleotides) # define self.string_of_nucleotides as string_of_nucleotides transformed into a list.
        elif isinstance(string_of_nucleotides, list): # if it is a list
            self.string_of_nucleotides = string_of_nucleotides # define self.string_of_nucleotides as the list.
        else: # otherwise.
            raise TypeError("Use a string to initialize the sequence or a list of nucleotides") # raise an error.
            
        if mutations== None: # if there are no mutations.
            self.mutations = [0]*len(string_of_nucleotides) # create a list named self.mutations of the same lenght as the string of nucleotides.
        else: # if there is something inside mutations.
            self.mutations = mutations # assign mutations to self.mutations. 
    
    
    def nucleotide_at_position(self, position): # define a function nuceleotide_at_position that takes as argument self and position.
        return self.string_of_nucleotides[position] # return the nucleotide at the position taken as argument.
 
 
    def sequence_length(self): # define a function sequence_length that takes as argument self.
        return len(self.mutations) # return the length of the mutations list (length of the sequence).
    
    
    def get_name(self): # define a function get_name that takes as argument self.
        return self.name # return the name.
   
    
    def copy(self, new_name): # define a function copy that takes as argument self and new_name.
        # return a sequence that contains the new name, a the string of nucleotides and the mutations at each position.
        return Sequence(new_name,self.string_of_nucleotides.copy(),self.mutations.copy())
    
    
    def __str__(self): # define __str__ that takes as argument self.
        return self.name + ' : ' + str(self.string_of_nucleotides) # return the name and the chain as a string.
    
    
    def mutate_nucleotide_at_position(self,position,nucleotide): # define a function that takes as argument self, position and nucleotide.
        '''
        this function will mutate a nucleotide at the postition given as argument.
        '''
        if (nucleotide!=self.string_of_nucleotides[position]): # if the nucleotide given as argument is different than the nucleotide at the given position in string_of_nucleotides.
            self.mutations[position] = self.mutations[position] + 1 # add a mutation to that position.
        
        self.string_of_nucleotides[position] = nucleotide # change the nucleotide at the given position for the new nucleotide.
        
        
    def get_number_of_mutations_at_each_position(self): # define a function that takes self as argument.
        return self.mutations # return the mutations list, that contains the mutations at each position.


def main(): # define the main function to prove that the class works well.
    
    sequence_a = Sequence("First_Species", list("ACTGACTG")) # store a sequence_a 'First species' and a sequence.
    sequence_b = sequence_a.copy("Second_Species") # copy sequence_a but with 'Second_species' instead of 'First_species'.
    
    # call the mutate_nucleotide_at_position function.
    sequence_a.mutate_nucleotide_at_position(1, "C") # mutate the position 1 of sequence_a by a 'C'.
    sequence_b.mutate_nucleotide_at_position(2, "A") # mutate the position 2 of sequence_b by an 'A'.
    
    print(sequence_a) # print sequence_a with the mutation.
    print(sequence_b) # print sequence_b with the mutation.
    print("")
    
    print(sequence_a.get_number_of_mutations_at_each_position()) # print the number of mutations at each position of sequence_a. There are no mutations because the the non-mutated nucleotide was the same than the mutated.
    print(sequence_b.get_number_of_mutations_at_each_position()) # print the number of mutations at each position of sequence_b.
    
    
if __name__ == "__main__":
    main () 