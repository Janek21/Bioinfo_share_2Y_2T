# Homology modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env,
              alnfile  = 'aln9.pir', # alignment filename
              knowns   = ('1mc5A'),     # codes of the templates #NOM QUE LI HAS POSAT AL PAS DEL PERL(splitchain), L ULTIM ARGUMENT 
              sequence = 'target')               # code of the target (name of the protein in the fasta)
a.starting_model= 1                 # index of the first model
a.ending_model  = 2                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modeling