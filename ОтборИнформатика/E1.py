
n = int(input())
a = list(map(int, input().split()))
res = 0

for i in range(n):
  j = i + 1
  if j > len(a):
    
  if i != j:
    r = (a[i] - a[j]) ** 2
    res += r
    
print(res)