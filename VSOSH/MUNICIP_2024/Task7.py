# Задача 7. Благоустройство

# решение Максима, вариант 1

# жадный алгоритм

d = 3
n = 5
x = [2,3,6,9,10]
res = []
res.append(x[0])
for i in range(1,n):
  if x[i-1] + d <= x[i]:
    res.append(x[i])
print(res)
