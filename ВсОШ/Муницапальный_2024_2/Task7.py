# Задача 7. Задачи на печать!

# решение Максима, вариант 1

n = 0
x = []
c = 0
prev_type = None # 1 or 2
for i in range(n):
  cur_t = x[i]
  if prev_type == 2:
    if cur_t == 1:
      prev_type = 1
      c += 1
    if cur_t == 3:
      prev_type = 1
      c += 1
  elif prev_type == None:
    if cur_t == 1:
      prev_type = 1
      c += 1
    elif cur_t == 2:
      prev_type = 2
      c += 1
    else:
      if i+1 <= n:
        c += 1
        if x[i+1] == 1:
          prev_type = 1
        else:
          prev_type = 2
      else:
        break
  else:
    if cur_t == 2:
      prev_type = 2
      c += 1
    if cur_t == 3:
      prev_type = 2
      c += 1
