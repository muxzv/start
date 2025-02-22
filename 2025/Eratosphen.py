def visulize(num_list, i):
  res_list = ''
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
    #visulize(nums_list, i)

  for i in range(i, a+1):
    if nums_list[i]:
      simple_set.add(i)

  return simple_set,d

simples, divides = task_eratosphen(150)

print('simple:', simples)
print()
print('divides:', divides)
print()

def factorize_recursive(num,simples,divides,res=list()):
  if num in simples:
    res.append(num)
  else:
    divider = divides[num]
    res.append(divider)
    num2 = num // divider
    factorize_recursive(num2,simples,divides,res)
  return res
  
def factorize(num,simples,divides,res=list()):
  while num > 1:
    divider = num if num in simples else divides[num]
    res.append(divider)
    num //= divider
  return res

print(factorize(110,simples,divides))
