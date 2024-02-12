
def lcs(X, Y):

    m = len(X)
    n = len(Y)
    
    # Create a list of (m+1) x (n+1)
    # This will be used to store the lengths of the longest common subsequences
    L = [[0] * (n + 1) for x in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                # Increase 1
                L[i][j] = 1 + L[i - 1][j - 1]
            else:
                # If tthey are different, take the max of the previous values
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    return L[m][n],L


def minimum_supersequence(X, Y,L):
    supersequence = ""
    i, j = len(X), len(Y)
    
    # Iterate until both strings X and Y are full
    while i > 0 and j > 0:
        # If the characters are the same, add one of them to the supersequence
        if X[i - 1] == Y[j - 1]:
            supersequence = X[i - 1] + supersequence
            i -= 1
            j -= 1
        # If the character in X contributes to the LCS, add it
        elif L[i - 1][j] > L[i][j - 1]:
            supersequence = X[i - 1] + supersequence
            i -= 1
        # Else, add the character in Y to the supersequence
        else:
            supersequence = Y[j - 1] + supersequence
            j -= 1
    while i > 0:
        supersequence = X[i - 1] + supersequence
        i -= 1
    while j > 0:
        supersequence = Y[j - 1] + supersequence
        j -= 1
    
    return supersequence


S1 = "GCACG"
S2 = "CATGT"

lcs_length, L = lcs(S1, S2)
print( minimum_supersequence(S1, S2, L))

