def fibanan(n):
  if n == 0 or n == 1:
    return 1
  n = fibanan(n - 1) + fibanan(n - 2)
  print(n)
  return n

def Task(n):
  for e in range(1,n+1):
    print(fibanan(e))

def Task2(n):
  fibanan(n)

#Task2(10)

def fact(n):
  if n == 0 or n == 1:
    return 1
  a = n * fact(n-1)
  print(n,a)
  return a

def FactFirst(n):
  print(fact(n))
  
FactFirst(5)
