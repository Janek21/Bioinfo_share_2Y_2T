#!/usr/bin/python3

import textwrap

class Seq(object):

    #constructor

    def __init__(self, id="", seq=""):
        self.id=id
        self.seq=seq
        self.print_fasta()

    #output when class is called
        
    def __str__(self):
        return self.multiline_printer()

    #generate the dictionary {"header": "sequence"} while adding > to header
        
    def print_fasta(self):
        fasta_list={}
        header=">"+self.id
        fasta_list[header]=self.seq
        return(fasta_list)
    
    #print the previous dictionary with header in one line and sequence in the next one (line break at 60char)

    def multiline_printer(self):
        fasta_dict=self.print_fasta()
        for entry in fasta_dict:
            print(entry)
            if list(fasta_dict)[-1]==entry:#in last read no line jump, return will already do so, that way there is no extra line
                print(textwrap.fill(fasta_dict[entry], 60), end="") 
            else:
                print(textwrap.fill(fasta_dict[entry], 60))
        return ""

def main():
    '''
        >>> record = Seq()
        >>> record.id = "FAST_CAT"
        >>> record.seq = "FASTCAT"
        >>> print(record)
        >FAST_CAT
        FASTCAT
        >>> record = Seq()
        >>> record.id = "MANY_CATS"
        >>> record.seq = "CAT"*100
        >>> print(record)
        >MANY_CATS
        CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
        CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
        CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
        CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
        CATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
    '''
    record=Seq()
    record.id="FAST_CAT"
    record.seq="FASTCAT"
    print(record)
    return

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)