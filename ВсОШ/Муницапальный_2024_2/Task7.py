# Задача 7. Задачи на печать!

# решение Максима, вариант 1

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