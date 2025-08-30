# Задача 1C. Цветная бумага

# решение Максима, вариант 1

def fill_sq(x,y,l):
  for i in range(x, x+10):
    for j in range(y, y+10):
      if i <= 100 and y <= 100:
        l[j][i] = 1


n = int(input())

x, y = [], []

for _ in range(n):
  a = list(map(int, input().split()))
  x.append(a[0])
  y.append(a[1])
  
l = [[0] * 100] * 100

for i in range(n):
  fill_sq(x[i], y[i])
  
print(l)
