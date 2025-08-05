l = list(map(int, input().split()))

n = l[0]
k = l[1]

dp = [1] * n
dp[0] = 2

z = 1

for i in range(1,n):
  if z == k:
    z = 0
  else:
    dp[i] += 1
    z += 1

c = 1
for e in dp:
  c *= e

print(c + 1)
print(dp)
