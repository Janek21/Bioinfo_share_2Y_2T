def indexing(text):
  """
  This function returns a sorted list of tuples containing all possible offsets of the substrings in the string.

  Args:
      text: The string to be indexed.

  Returns:
      A sorted list of tuples containing all possible offsets of the substrings in the string.
      Each tuple has two elements: the substring and a sorted list of offsets for this substring in the string.
  """
  res = []
  for i in range(len(text)):
    for j in range(i, len(text)):
      sub = text[i:j+1]
      for k, (s, offsets) in enumerate(res):
        if s == sub:
          offsets.append(i)
        else:
            res.append((sub, [i]))
  for _, offsets in res:
    offsets.sort()  # Sort offsets within each tuple
  res.sort()
  return res


text = "abab"
print(indexing(text))