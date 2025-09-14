n = int(input())
nl = [i for i in range(1,n*n+1)]

nm = [[0 for i in range(n)] for j in range(n)]

m = n // 2

for i in range(m+1):
  for j in range(m-i, m+i+1):
    nm[i][j] = 1
    nm[n-i-1][j] = 1

chet = []
nechet = []
for e in nl:
  if e % 2 == 0:
    chet.append(e)
  else:
    nechet.append(e)

aa = -1
for i in range(n):
  for j in range(n):
    num = nm[i][j]
    if num % 2 == 0:
      nm[i][j] = chet.pop()
    else:
      nm[i][j] = nechet.pop()

for e in nm:
  print(*e)