n = int(input())
a = list(map(int, input().split()))
res = 0

d = dict()

for i in range(n):
  for j in range(i+1,n):
    #print(j)
    da = a[i] - a[j]
    if da in d.keys():
      res += d[da]
    else:
      aaa = da * da
      res += aaa
      d[da] = aaa

print(res)