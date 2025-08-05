num = int(input())

if num == 0 or num == 1:
  print(1)
else:
  a = [0] * (num * 3)
  a[0] = 1
  a[1] = 1
  for i in range(2, num + 1):
    n = i // 2
    if i % 2 == 0:
      a[i] = a[n] + 1
    else:
      a[i] = a[n] + a[n + 1] + 1
  print(a[num])
