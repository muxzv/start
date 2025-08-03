n = int(input())

dp = [0] * (n + 1)

for i in range(2, n+1):
  xone = dp[i-1]
  xtwo = 10 ** 7
  xthree = 10 ** 7
  if i % 2 == 0:
    xtwo = dp[i // 2]
  if i % 3 == 0:
    xthree = dp[i // 3]
  xbest = min(xone, xtwo, xthree)
  dp[i] = xbest + 1
  
print(dp[-1])
