'''

@author: olao
'''


class Sequence(object):
    '''
    classdocs
    '''


    def __init__(self, name, string_of_nucleotides,mutations=None):
        '''
        Constructor
        '''
        self.name = name
        
        if isinstance(string_of_nucleotides, str):
            self.string_of_nucleotides = list(string_of_nucleotides)
        elif isinstance(string_of_nucleotides,list):
            self.string_of_nucleotides = string_of_nucleotides
        else:
            raise TypeError("Use a string to initialize the sequence or a list of nucleotides")
            
            
        if mutations== None:
            self.mutations = [0]*len(string_of_nucleotides)
        else:
            self.mutations = mutations        
    
    
    def nucleotide_at_position(self,position):
        return self.string_of_nucleotides[position]
 
 
    def sequence_length(self):
        return len(self.mutations)
    
    
    def get_name(self):
        return self.name
   
    
    def copy(self, new_name):
        return Sequence(new_name,self.string_of_nucleotides.copy(),self.mutations.copy())
    
    
    def __str__(self):
        return self.name + ' : ' + str(self.string_of_nucleotides)
    
    
    def mutate_nucleotide_at_position(self,position,nucleotide):
        if(nucleotide!=self.string_of_nucleotides[position]):
            self.mutations[position] = self.mutations[position] + 1
        
        self.string_of_nucleotides[position] = nucleotide
        
        
    def get_number_of_mutations_at_each_position(self):
        return self.mutations


    
def main():
    
    sequence_a = Sequence("First_Species", list("ACTGACTG"))
    sequence_b = sequence_a.copy("Second_Species")
    
    sequence_a.mutate_nucleotide_at_position(1, "C")
    sequence_b.mutate_nucleotide_at_position(2, "A")    
    
    print(sequence_a)
    print(sequence_b)
    print("")
    
    print(sequence_a.get_number_of_mutations_at_each_position())
    print(sequence_b.get_number_of_mutations_at_each_position())
    
    
if __name__ == "__main__":
    main () 
