def visulize(num_list, i):
  if i < 10:
    res_list = " ";
  res_list += str(i) + " "

  for e in num_list[2:]:
    if e:
      res_list += 'o'
    else:
      res_list += 'x'
  print(res_list)

def task_eratosphen(a):
  
  nums_list = [True for i in range(a+1)]
  
  d = {}
  
  sqr_a = a ** 0.5
  
  simple_set = set()
  
  for i in range(2, a+1):
    if i**2 > a:
      break
    if nums_list[i]:
      simple_set.add(i)
    for j in range(i*i, a+1, i):
      nums_list[j] = False
      if not j in d:
        d[j] = i
    visulize(nums_list, i)

  for i in range(i, a+1):
    if nums_list[i]:
      simple_set.add(i)

  return simple_set,d

simples, divides = task_eratosphen(20)

print('simple:', simples)
print()
print('divides:', divides)
