def task_eratosphen(a):
  
  nums_dict = [True for i in range(a+1)]
  
  sqr_a = a ** 0.5
  
  res = []
  
  for i in range(2, a+1):
    if i > sqr_a:
      break
    if nums_dict[i]:
      res.append(i)
    for j in range(i*i, a+1, i):
      nums_dict[j] = False
    
  for i in range(i, a+1):
    if nums_dict[i]:
      res.append(i)
  
  return res

print(task_eratosphen(100))
