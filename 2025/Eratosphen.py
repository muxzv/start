def task_eratosphen(a):
  
  nums_list = [True for i in range(a+1)]
  
  sqr_a = a ** 0.5
  
  simple_set = set()
  
  for i in range(2, a+1):
    if i > sqr_a:
      break
    if nums_list[i]:
      simple_set.add(i)
    for j in range(i*i, a+1, i):
      nums_list[j] = False
    
  for i in range(i, a+1):
    if nums_list[i]:
      simple_set.add(i)
  
  return simple_set

print(task_eratosphen(100))
