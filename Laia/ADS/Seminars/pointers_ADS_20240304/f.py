
def f(b):
  global a
  b = list(b)
  print('a:', a)
  print('b:', b)
  b[0] = 42
  print('a:', a)
  print('b:', b)


