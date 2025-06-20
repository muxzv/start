from functools import lru_cache

@lru_cache() #помогает сохранять ранее полученнее значения фурнкции
def fibanan2(n):
  global c
  c += 1
  if n <= 2:
    e = 1
  else:
    e = fibanan(n - 1) + fibanan(n - 2)
  return e

def fibanan(n,d = None):
  global c
  if d != None and n in d:
    return d[n]
  c += 1
  if n <= 2:
    e = 1
  else:
    e = fibanan(n - 1,d) + fibanan(n - 2,d)
  if d != None:
    d[n] = e
  return e

def FibananFirst(n):
  d = {}
  fibanan(n,d)
  return d

c = 0

print(FibananFirst(11))
print('Кол-во вызовов с кэшированием:', c)

c = 0

print(fibanan(11))
print('Кол-во вызовов без кэширования:', c)

c = 0

print(fibanan2(11))
print('Кол-во вызовов с кэшированием:', c)

##############################################################

def fact(n,d):
  if n < 0:
    raise BaseException('Err')
  if n in d:
    return d[n]
  a = n * fact(n-1,d)
  d[n] = a
  return a

def FactFirst(n):
  d = {0:1, 1:1}
  fact(n,d)
  return d

#print(FactFirst(5))
