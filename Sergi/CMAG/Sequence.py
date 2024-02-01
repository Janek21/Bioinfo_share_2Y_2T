'''

@author: Sergi Ocaña Alamo
'''

#Start a class called Sequence
class Sequence(object):
    '''
    classdocs
    '''
    #Start the constructor with self, name string_of_nucleotides and mutations
    def __init__(self, name, string_of_nucleotides, mutations=None):
        '''
        Constructor
        '''
        # Assign a name 
        self.name = name

        # Check if  nucleotides are put it as a string
        if isinstance(string_of_nucleotides, str):
            # If it's a string, convert it to a list of characters
            self.string_of_nucleotides = list(string_of_nucleotides)
        # If it's already a list, use it as is
        elif isinstance(string_of_nucleotides, list):
            self.string_of_nucleotides = string_of_nucleotides
        else:
            # Raise a TypeError if the input is neither a string nor a list
            raise TypeError("Use a string to initialize the sequence or a list of nucleotides")

        # Check if mutations parameter is provided, if not, begin with zeros
        if mutations is None:
            self.mutations = [0] * len(string_of_nucleotides)
        else:
            # If provided yes, use the actual  list
            self.mutations = mutations

    def nucleotide_at_position(self, position):
        # Return the nucleotide at the position
        return self.string_of_nucleotides[position]

    def sequence_length(self):
        # Return the length of the sequence
        return len(self.mutations)

    def get_name(self):
        # Return the name of the sequence
        return self.name

    def copy(self, new_name):
        # Create and return a new Sequence object with the same nucleotides and mutations
        return Sequence(new_name, self.string_of_nucleotides.copy(), self.mutations.copy())

    def __str__(self):
        # Return a string of the sequence, including name and nucleotides
        return self.name + ' : ' + str(self.string_of_nucleotides)

    def mutate_nucleotide_at_position(self, position, nucleotide):
        # Check if the new nucleotide is different from the actual one, and update if necessary
        if nucleotide != self.string_of_nucleotides[position]:
            self.mutations[position] += 1

        # Update the nucleotide at the specified position
        self.string_of_nucleotides[position] = nucleotide

    def get_number_of_mutations_at_each_position(self):
        # Return the list of mutations for each position in the sequence
        return self.mutations


def main():
    # Create a Sequence object 'sequence_a' with the name "First_Species" and nucleotides "ACTGACTG"
    sequence_a = Sequence("First_Species", list("ACTGACTG"))

    # Create a copy 'sequence_b' of 'sequence_a' 
    sequence_b = sequence_a.copy("Second_Species")

    # Mutate nucleotide at position 1 in 'sequence_a' to "C"
    sequence_a.mutate_nucleotide_at_position(1, "C")

    # Mutate nucleotide at position 2 in 'sequence_b' to "A"
    sequence_b.mutate_nucleotide_at_position(2, "A")

    # Print the strings of 'sequence_a' and 'sequence_b'
    print(sequence_a)
    print(sequence_b)
    print("")

    # Print the number of mutations at each position of 'sequence_a' and 'sequence_b'
    print(sequence_a.get_number_of_mutations_at_each_position())
    print(sequence_b.get_number_of_mutations_at_each_position())


if __name__ == "__main__":
    main()
