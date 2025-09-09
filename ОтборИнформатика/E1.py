n = int(input())
a = list(map(int, input().split()))
res = [0,0]

for e in a:
  res[0] += e
  res[1] += e*e

print(n * res[1] - res[0] * res[0])