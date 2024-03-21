def hamming_distance(seq1, seq2):
    
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length Arnau el doctest bien porfavor")

    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1

    return distance


sequence = "Corolla"
sequence2 = "Avensis"
distance = hamming_distance(sequence, sequence2)
print("Hamming distance '{}' and '{}' is {}".format(sequence, sequence2, distance))
