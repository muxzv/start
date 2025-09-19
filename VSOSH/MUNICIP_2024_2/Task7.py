# Задача 7. Задачи на печать!

# style - True - 2-сторонная - double
# style - False - 1-сторонная - single

n = int(input())
x = []
for _ in range(n):
  x.append(int(input()))
mode = 0 # 1 or 2 or 0

c = 0
for e in x:
  if mode == 0:
    if e == 1:
      mode = 1
    elif e == 2:
      mode = 2
    c += 1

  elif mode == 1:
    if e == 2:
      mode = 2
      c += 1
    elif e == 3:
      mode = 2
      c += 1
  
  elif mode == 2:
      if e == 1:
        mode = 0
      elif e == 3:
        mode = 0

print(c)