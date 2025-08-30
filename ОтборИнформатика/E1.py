# Задача 1E. Коллекция

# решение Максима, вариант 1

a = [2, 8, 4]

res = 0

for i in a:
  for j in a:
    if i != j:
      r = (a[i] - a[j]) ** 2
      res += r
    
print(res)
