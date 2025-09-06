# Задача 1C. Цветная бумага

# решение Максима, вариант 1

def fill_sq(x,y,l):
  for i in range(x,x+10):
    for j in range(y,y+10):
      if i <= 100 and j <= 100:
        l[i][j] = 1

n = 0 #int(input())

l = [[0]*100] * 100
nl = [[1,1]]
for e in nl:
  fill_sq(e[0],e[1],l)

for e in l:
  print(e)