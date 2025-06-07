#Задача
#У вас есть 𝑛 прямоугольных дипломов размера 𝑎 × 𝑏. Вы хотите повесить их на
#квадратную доску наименьшего размера так, чтобы их все было видно, то есть
#чтобы они никак не накладывались. Поворачивать дипломы нельзя.

def f(x,a,b):
  return (x // a)*(x // b)

def check(x, n, a, b):
  return f(x,a,b) >= n

def task(a,b,n,l,r):
  
  while r - l > 1:
    mid = (l + r) // 2
    if check(mid, n, a, b):
      r = mid
    else:
      l = mid
  
  return r

a = 1
b = 2

n = 4

l = 0
r = n*max(a, b)

print(task(a,b,n,l,r))
