# Задача 7. Задачи на печать!

# style - True - 2-сторонная - double
# style - False - 1-сторонная - single

<<<<<<< HEAD
n = 4 #int(input())
x = []
for _ in range(n):
    x.append(int(input()))
mode = 0 # 1 or 2 or 0


for e in x:
    if mode == 0:
      if e == 1:
        mode = 1
      elif e == 2:
        mode = 2
      c += 1

    if mode == 1:
      if e == 2:
        mode = 2
        c += 1
      elif e == 3:
        mode = 2
        c += 1
    
    if mode == 2:
        if e == 1:
          mode = 0
        elif e == 3:
          mode = 0

print(c)
=======
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
>>>>>>> d93e8760402de4de10f23f7dc63bdb8ed25f6a53
