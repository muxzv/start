n = int(input())

if n == 0 or n == 1:
  print(1)
else:
  a = [0] * n
  a[0] = 1
  a[1] = 1
  for i in range(2, n):
    if i % 2 == 0:
      a[2 * i] = a[i] + 1
    else:
      a[2 * i + 1] = a[2 * n + 1] - a[i]

print(a)
