from Bio.Align import substitution_matrices
from fasta2dict import fasta2dict


def align_profiles(seq_dict1, seq_dict2, gap):
    """Makes a profile alignment of sequences with names name_i
    and name_j, whose sequences are in seqs, a dictionary of sequences
    with names (as keys)
    >>> align_profiles(fasta2dict('cats.fasta'), fasta2dict('rats.fasta'), -4)
    (10.25, {'FAST_CAT': 'thefastcat', 'FAT_CAT': 'a--fa-tcat', 'A_RAT': 'a--ra-t---', 'THE_RATS': 'thera-t--s'})
    """
    subst_mat = substitution_matrices.load("BLOSUM62")
    len_i = len(list(seq_dict1.values())[0])
    len_j = len(list(seq_dict2.values())[0])

    # initialization
    score_mat = [[0 for _ in range(len_j + 1)] for _ in range(len_i + 1)]
    traceback = [[0 for _ in range(len_j + 1)] for _ in range(len_i + 1)]

    for i in range(len_i + 1):
        score_mat[i][0] = i * gap
        traceback[i][0] = 1

    for j in range(len_j + 1):
        score_mat[0][j] = j * gap
        traceback[0][j] = -1

    # Compute the scores
    for i in range(1, len_i + 1):
        for j in range(1, len_j + 1):
            score = 0
            num_subst = 0

            for val1 in seq_dict1.values():

                for val2 in seq_dict2.values():
                    if val1[i-1]!="-" and val2[j-1]!="-":

                        score += subst_mat[val1[i-1].upper()][val2[j-1].upper()]
                        num_subst += 1
            
            if num_subst > 0:
                score = score / num_subst 
            
            subst = score_mat[i - 1][j - 1] + score
            delet = score_mat[i][j - 1] + gap
            inser = score_mat[i - 1][j] + gap

            if subst >= delet and subst >= inser:
                score_mat[i][j] = subst
                traceback[i][j] = 0
            elif delet >= inser:
                score_mat[i][j] = delet
                traceback[i][j] = -1
            else:
                score_mat[i][j] = inser
                traceback[i][j] = 1

    # Traceback
    i, j = len_i, len_j

    ali_seqs = {}
    for seq_i in seq_dict1:
        ali_seqs[seq_i] = []
    for seq_j in seq_dict2:
        ali_seqs[seq_j] = []

    while i != 0 or j != 0:
        if traceback[i][j] == 0:
            i -= 1
            j -= 1
            for name_i, seq_i in seq_dict1.items():
                ali_seqs[name_i].append(seq_i[i])
            for name_j, seq_j in seq_dict2.items():
                ali_seqs[name_j].append(seq_j[j])
        elif traceback[i][j] == -1:
            j -= 1
            for name_i, seq_i in seq_dict1.items():
                ali_seqs[name_i].append("-")
            for name_j, seq_j in seq_dict2.items():
                ali_seqs[name_j].append(seq_j[j])
        else:
            i -= 1
            for name_i, seq_i in seq_dict1.items():
                ali_seqs[name_i].append(seq_i[i])
            for name_j, seq_j in seq_dict2.items():
                ali_seqs[name_j].append("-")

    seqs = {name: "".join(reversed(seq)) for name, seq in ali_seqs.items()}
    return score_mat[-1][-1], seqs

if __name__=="__main__":
	import doctest
	doctest.testmod(verbose=True)