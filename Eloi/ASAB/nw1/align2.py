from Bio.Align import substitution_matrices
from Bio import SeqIO
import sys

def trace(M, seq1, seq2, j, i):
    # Trace back through the matrix to find the aligned sequences
    res1, res2 = [], []
    
    while (i, j) != (0, 0):
        match, gap, mismatch = M[i-1][j-1], M[i-1][j], M[i][j-1]

        # Choose the direction based on the values in the matrix
        if match >= max(mismatch, gap):
            res1.append(seq1[j])
            res2.append(seq2[i])
            i -= 1
            j -= 1
        elif gap <= mismatch:
            res1.append(seq1[j])
            res2.append('-')
            j -= 1
        else:
            res1.append('-')
            res2.append(seq2[i])
            i -= 1

    # Return the reversed sequences
    return ''.join(reversed(res1)), ''.join(reversed(res2))

def nw(seq1, seq2, subst_mat, gap_penalty):
    # Initialize sequences
    seq1, seq2 = '-' + seq1, '-' + seq2
    # Initialize matrix
    M = [[-x if y == 0 else -y if x == 0 else 0 for x in range(len(seq1))] for y in range(len(seq2))]

    # Fill in the matrix using the Needleman-Wunsch algorithm
    for i in range(1, len(seq2)):
        for j in range(1, len(seq1)):
            pos_m, pos_g, pos_mis = M[i-1][j-1], M[i-1][j], M[i][j-1]
            sub_score = subst_mat[seq1[j]][seq2[i]]

            if seq1[j] == seq2[i]:
                M[i][j] = pos_m + sub_score
            else:
                M[i][j] = max(pos_mis + gap_penalty, pos_g + gap_penalty, pos_m + gap_penalty)

    # Return the matrix and modified sequences
    return M, seq1, seq2

def get_alignment(result_trace, subst_mat, gap_penalty):
    # Create representations of aligned sequences and calculate total score
    repre1, repre2, score, score_total = [], [], [], 0

    for y in range(len(result_trace[0])):
        if '-' in (result_trace[0][y], result_trace[1][y]):
            repre1.append(result_trace[0][y])
            repre2.append(result_trace[1][y])
            score.append('·')
            score_total += gap_penalty
        elif result_trace[0][y] == result_trace[1][y]:
            repre1.append(result_trace[0][y])
            repre2.append(result_trace[1][y])
            score.append('*')
            score_total += subst_mat[result_trace[0][y]][result_trace[1][y]]
        elif result_trace[0][y] != result_trace[1][y]:
            repre1.append(result_trace[0][y])
            repre2.append(result_trace[1][y])
            score.append(' ')
            score_total += subst_mat[result_trace[0][y]][result_trace[1][y]]

    # Create a formatted result for each block of 40 characters
    result = [f"{' '.join(repre1[i:i+40])}\n{' '.join(['|' if amino != '' else '' for amino in repre1[i:i+40]])}\n{' '.join(repre2[i:i+40])}\n{' '.join(score[i:i+40])}\n" for i in range(0, len(repre1), 40)]
    return result, score_total

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python align2.py <filename> <seq1> <seq2> <gap_penalty>")
        sys.exit(1)

    # Extract command line arguments
    filename, name1, name2, gap_penalty = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])

    # Load the BLOSUM62 substitution matrix
    subst_mat = substitution_matrices.load("BLOSUM62")

    seq1, seq2 = '', ''
    records = SeqIO.parse(filename, 'fasta')

    # Extract sequences based on provided names
    for record in records:
        ID = record.name.split('|')[2]
        if ID == name1:
            seq1 = record.seq
        if ID == name2:
            seq2 = record.seq

    # Check if sequences are found
    if not seq1 or not seq2:
        print("No records found in the fasta file")
        sys.exit(1)

    # Perform Needleman-Wunsch alignment
    M, seq1, seq2 = nw(str(seq1), str(seq2), subst_mat, gap_penalty)
    # Trace back to get the aligned sequences
    result_trace = trace(M, seq1, seq2, len(seq1)-1, len(seq2)-1)
    # Get the alignment representation and total score
    alignment_representation = get_alignment(result_trace, subst_mat, gap_penalty)
    
    # Print the total score and alignment representation
    print(alignment_representation[1], result_trace)
    
    # Write the results to a file
    with open(f'{filename}_ALIGNMENT.txt', 'w') as output_file:
        output_file.write(f'>>{name1} and {name2} alignment:\n\n')
        for line in alignment_representation[0]:
            output_file.write(f'{line}\n\n')
        output_file.write("Total score: " + str(alignment_representation[1]))
