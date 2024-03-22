from Bio.Align import substitution_matrices
from fasta2dict import fasta2dict


def align_profiles(seqs, names_i, names_j, gap):
    """Makes a profile alignment of sequences with names name_i
    and name_j, whose sequences are in seqs, a dictionary of sequences
    with names (as keys)
    >>> align_profiles(fasta2dict('cats_and_rats.fasta'), ['FAST_CAT', 'FAT_CAT'], ['A_RAT', 'THE_RATS'], -4)
    (10.25, {'FAST_CAT': 'thefastcat', 'FAT_CAT': 'a--fa-tcat', 'A_RAT': 'a--ra-t---', 'THE_RATS': 'thera-t--s'})
    >>> align_profiles(fasta2dict('hmgb.fasta'), ['hmgt_mouse'], ['hmgl_trybr', 'hmgl_wheat', 'hmgb_chite'], -4)[0]
    -20.0
    """
    subst_mat = substitution_matrices.load("BLOSUM62")
    len_i, len_j = len(seqs[names_i[0]]), len(seqs[names_j[0]])
    score_mat = [[0] * (len_j + 1) for _ in range(len_i + 1)]
    traceback = [[0] * (len_j + 1) for _ in range(len_i + 1)]

    for i in range(len_i + 1):
        score_mat[i][0], traceback[i][0] = i * gap, 1

    for j in range(len_j + 1):
        score_mat[0][j], traceback[0][j] = j * gap, -1

    for i in range(1, len_i + 1):
        for j in range(1, len_j + 1):
            
            score = 0
            num_subst = 0

            for n_i in names_i:

                for n_j in names_j:
                    if seqs[n_i][i-1]!='-' and seqs[n_j][j-1]!='-':

                        score += subst_mat[seqs[n_i][i-1].upper()][seqs[n_j][j-1].upper()]
                        num_subst += 1
            
            if num_subst > 0:
                score = score / num_subst  


            subst, delet, inser = (
                score_mat[i - 1][j - 1] + score,
                score_mat[i][j - 1] + gap,
                score_mat[i - 1][j] + gap,
            )

            if subst >= delet and subst >= inser:
                score_mat[i][j], traceback[i][j] = subst, 0
            elif delet >= inser:
                score_mat[i][j], traceback[i][j] = delet, -1
            else:
                score_mat[i][j], traceback[i][j] = inser, 1

    i, j = len_i, len_j
    ali_seqs = {name: [] for name in names_i + names_j}

    while i != 0 or j != 0:
        if traceback[i][j] == 0:
            i, j = i - 1, j - 1
            for ii in names_i:
                ali_seqs[ii].append(seqs[ii][i])
            for jj in names_j:
                ali_seqs[jj].append(seqs[jj][j])
        elif traceback[i][j] == -1:
            j -= 1
            for ii in names_i:
                ali_seqs[ii].append("-")
            for jj in names_j:
                ali_seqs[jj].append(seqs[jj][j])
        else:
            i -= 1
            for ii in names_i:
                ali_seqs[ii].append(seqs[ii][i])
            for jj in names_j:
                ali_seqs[jj].append("-")

    for name, seq in ali_seqs.items():
        seqs[name] = "".join(reversed(seq))
    return score_mat[-1][-1], seqs

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)