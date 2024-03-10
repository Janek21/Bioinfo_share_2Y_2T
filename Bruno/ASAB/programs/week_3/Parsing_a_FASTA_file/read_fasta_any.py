def read_fasta(filename):
    '''
    >>> len(read_fasta("ppar.fasta"))
    133
    >>> seq_dict = read_fasta("ppar.fasta")
    >>> seq_dict['sp|P62987|RL40_HUMAN Ubiquitin-60S ribosomal protein L40 OS=Homo sapiens OX=9606 GN=UBA52 PE=1 SV=2']
    'MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGGIIEPSLRQLAQKYNCDKMICRKCYARLHPRAVNCRKKKCGHTNNLRPKKKVK'
    '''
    file_path = '/home/bruno/ESCI/2nd_year/2nd_term/ASAB_Algorithms_for_Sequence_Analysis_in_Bioinformatics/programs/week_3/Parsing_a_FASTA_file/' + filename
    Dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line[0] == '>':
                key = line[1:].strip()
                Dict[key] = ''
            else:
                Dict[key] += line.strip()
    return Dict

if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)