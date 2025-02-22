def task_eratosphen(b, a):
  
  
  nums_list = [True for i in range(a+1)]
  
  sqr_a = a ** 0.5
  
  simple_set = list()
  
  if a in (2, 3):
    simple_set.append(2)
  
  i = 2

  for i in range(2, int(a**0.5) + 1):
    if nums_list[i]:
      if i >= b:
        simple_set.append(i)
      for j in range(i*i, a+1, i):
          nums_list[j] = False

  for i in range(i+1, a+1):
    if nums_list[i]:
      if i > b:
        simple_set.append(i)

  return simple_set

a,b = map(int,input().split())

simples = task_eratosphen(a,b)
if len(simples) == 0:
  print(-1)
else:
  for e in simples:
    print(e)
