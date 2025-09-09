n = int(input())
a = list(map(int, input().split()))
res = 0

d = dict()

for i in range(n):
  for j in range(i+1,n):
    #print(j)
    delta = abs(a[i] - a[j])
    if delta in d.keys():
      res += d[delta]
    else:
      delta2 = delta * delta
      d[da] = delta2
      res += delta2

print(res)
