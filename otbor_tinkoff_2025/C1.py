# Задача 1C. Цветная бумага

# решение Максима, вариант 1

def fill_sq(x,y,l,h):
  for i in range(x,x+10):
    for j in range(y,y+10):
      if i < h and j < h:
        l[i][j] = 1

def show(l):
  print('*' * len(l))
  for e in l:
    print(e)
  print('*' * len(l))

n = int(input())
h = 100
l = [[0 for _ in range(h)] for _ in range(h)]
nl = []
for _ in range(n):
  sa = list(map(int,input().split()))
  nl.append(sa)

for e in nl:
   fill_sq(e[0],e[1],l,h)

res = 0
for row in l:
    for element in row:
        if element == 1:
          res += 1
print(res)