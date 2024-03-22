from Bio import SeqIO

filename = "/home/sergi/Escritorio/ASAB/Arnau_Part/msa.fasta"
def count_basic_residues(sequence):
    basic_residues = ['R', 'K', 'H']
    count = sum(1 for residue in sequence if residue in basic_residues)
    return count

count_sequences = 0
with open(filename, "r") as fasta_file:
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence = str(record.seq)
        if count_basic_residues(sequence) >= 20:
            count_sequences += 1

print(f"Number of sequences containing 20 or more basic residues: {count_sequences}")
