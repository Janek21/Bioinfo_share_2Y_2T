from Bio import SeqIO
from Bio.Align import substitution_matrices

def calculate_pairwise_identity(seq1, seq2):
    identical_columns = 0
    total_columns = 0

    subst_mat = substitution_matrices.load("BLOSUM62")

    # Iterate 
    for res1, res2 in zip(seq1, seq2):
        if res1 != '-' and res2 != '-':
            total_columns += 1
            if res1 == res2:
                identical_columns += 1

    pairwise_identity = identical_columns / total_columns if total_columns > 0 else 0
    return pairwise_identity

sequences = list(SeqIO.parse("align.fasta", "fasta"))

identity = calculate_pairwise_identity(str(sequences[0].seq), str(sequences[1].seq))
print("Pairwise identity:", identity)
