#!/usr/bin/python3

from read_fasta_oneline import read_fasta_oneline as read_fasta

def read_fasta_any(filename):
    '''
    >>> len(read_fasta_any("ppar.fasta"))
    133
    >>> seq_dict = read_fasta_any("ppar.fasta")
    >>> seq_dict['sp|P62987|RL40_HUMAN Ubiquitin-60S ribosomal protein L40 OS=Homo sapiens OX=9606 GN=UBA52 PE=1 SV=2']
    'MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGGIIEPSLRQLAQKYNCDKMICRKCYARLHPRAVNCRKKKCGHTNNLRPKKKVK'
    '''
    return read_fasta(filename)


print(len(read_fasta_any("ppar.fasta")))

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)