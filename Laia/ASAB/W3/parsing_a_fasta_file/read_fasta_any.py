def read_fasta(filename):
    '''
    >>> len(read_fasta("ppar.fasta"))
    133
    >>> seq_dict = read_fasta("ppar.fasta")
    >>> seq_dict['sp|P62987|RL40_HUMAN Ubiquitin-60S ribosomal protein L40 OS=Homo sapiens OX=9606 GN=UBA52 PE=1 SV=2']
    'MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGGIIEPSLRQLAQKYNCDKMICRKCYARLHPRAVNCRKKKCGHTNNLRPKKKVK'
    '''

    directory = '/home/laia/Desktop/ASAB/Week3/aa_material/'+ filename
    header2seq = {}
    with open(directory, 'r') as f:
        header = None
        sequence = ''
        
        for line in f:
            if line[0] == '>':
                if header:
                    header2seq[header] = sequence
                header = line[1:].strip()
                sequence = ''
            else:
                sequence += line.strip()
        
        if header:
            header2seq[header] = sequence
    
    return header2seq

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)