def score_seqs(seq1, seq2, match, mismatch, gap):
  '''
  >>> score_seqs("THEFASTCAT", "THEFATCAT-", 1, -1, -2)
  -1
  >>> score_seqs("THEFASTCAT", "THEFATCA-T", 1, -1, -2)
  1
  >>> score_seqs("THEFA-TCAT", "THEFASTCAT", 1, -1, -2)
  7
  >>> score_seqs("THEFASTCAT", "THE", 1, -1, -2)
  0
  >>> score_seqs("THE-FASTCAT", "THE-FASTCAT", 1, -1, -2)
  8
  '''
  if len(seq1) != len(seq2):
    return 0
  else:
    counter = 0
    for i in range(len(seq1)):
      if seq1[i] == '-' or seq2[i] == '-':
        counter += gap
      elif seq1[i] == seq2[i]:
        counter += match
      else:
        counter += mismatch
    return counter



if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
