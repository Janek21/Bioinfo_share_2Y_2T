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
        self.name = name #make it so all methods can access name
        
        if isinstance(string_of_nucleotides, str): #if the "input" string_of_nucleotides is a string transform it into a list 
            self.string_of_nucleotides = list(string_of_nucleotides) #make it so all methods can call string_of_nucleotides
        elif isinstance(string_of_nucleotides,list): #if string_of_nucleotides is already a list, make it so all methods can call it
            self.string_of_nucleotides = string_of_nucleotides
        else: #if string_of_nucleotides is not a string nor a list raise a Type Error
            raise TypeError("Use a string to initialize the sequence or a list of nucleotides")
            
            
        if mutations== None: #if no mutations are given in the object 
            self.mutations = [0]*len(string_of_nucleotides) #generate an array of the same number of 0 as nucleotides in string_of_nucleotides, meaning that there are no mutations

        else:
            self.mutations = mutations  #if mutations are given make it so all methods can access it
    
    
    def nucleotide_at_position(self,position): #given a position
        return self.string_of_nucleotides[position] #return the nucleotide at that position
 
 
    def sequence_length(self): #give the length of the sequence using the number of nucleotides that mutate or not (mutations object)
        return len(self.mutations) #use
    
    
    def get_name(self): #print the name of the sequence
        return self.name
    
    def copy(self, new_name): #rename the sequence, change only the name and maintain nucleotides and mutations
        return Sequence(new_name,self.string_of_nucleotides.copy(),self.mutations.copy())
    
    
    def __str__(self): #if class is called in a print or return output name:string_of_nucleotides
        return self.name + ' : ' + str(self.string_of_nucleotides)
    
    
    def mutate_nucleotide_at_position(self,position,nucleotide): #given a position and a nucleotide
        if(nucleotide!=self.string_of_nucleotides[position]): #if nucleotide is different than the nucleotide in that position of string_of_nucleotides
            self.mutations[position] = self.mutations[position] + 1 #add 1 to the "mutation index(level?)" of that position (mark that position as mutated)
        
        self.string_of_nucleotides[position] = nucleotide #change the nucleotide of string_of_nucleotides in the position into the given nucleotide
        #if the nucleotide changes, substitute it for the given one, and even if its the same as the one on the position
        
        
    def get_number_of_mutations_at_each_position(self): #output the mutation list (reports if there is a change in any nucleotide)
        return self.mutations


    
def main():
    
    sequence_a = Sequence("First_Species", list("ACTGACTG")) #To class Sequence give name First_Species and string-turned-list "ACTGACTG" that will be the variable string_of_nucleotides
    sequence_b = sequence_a.copy("Second_Species") #for the same sequence change the name to Second_Species
    #mutations are not provided, it will be a list of 8 zeroes
    
    sequence_a.mutate_nucleotide_at_position(1, "C") #for position 1 and nucleotide "C" execute the function in sequence 1
    #Position 1 is already C, nothing will change, mutation level won't increase
    sequence_b.mutate_nucleotide_at_position(2, "A") #for position 2 and nucleotide "A" execute the function in sequence 2
    #Position 2 is not A, its T, A will change to T, mutation level will increase to 1 in position 2
    
    print(sequence_a)
    print(sequence_b)
    print("")
    
    print(sequence_a.get_number_of_mutations_at_each_position()) #print mutation list
    print(sequence_b.get_number_of_mutations_at_each_position()) #print mutation list
    
    
if __name__ == "__main__":
    main () 
