def fibanan(n,d):
  if n < 1:
    raise BaseException('Err')
  if n in d:
    return d[n]
  e = fibanan(n - 1,d) + fibanan(n - 2,d)
  d[n] = e
  return n

def FibananFirst(n):
  d = {1:1, 2:1}
  fibanan(n,d)
  return d

print(FibananFirst(10))
  
#########################################################################################

def fact(n,d):
  if n < 1:
    raise BaseException('Err')
  if n in d:
    return d[n]
  a = n * fact(n-1,d)
  d[n] = a
  return a

def FactFirst(n):
  d = {1:1}
  fact(n,d)
  return d

print(FactFirst(5))
