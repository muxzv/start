# Задача 7. Задачи на печать!

# style - True - 2-сторонная - double
# style - False - 1-сторонная - single

# 1 = 1
# 2 = 2
# 3 = 2+1 = 1+2

def helper(a, start_style):
  c = 1 # кол-во групп
  cur_style = start_style
  need_add = False
  for e in a:
    if need_add:
      c += 1
      need_add = False
    if cur_style: # double
      if e != 2:
        need_add = True
        cur_style = False
    elif e != 1:
      need_add = True
      cur_style = True
  return c

def Task(a):
  if a[0] == 2:
    return helper(a, True)
  if a[0] == 1:
    return helper(a, False)
  else:
    return min(helper(a, True), helper(a, False))
    
print(Task([1, 3, 2, 1]))
print(Task([3, 3]))

print(Task([2, 1, 2, 1]))
