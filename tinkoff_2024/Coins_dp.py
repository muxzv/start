n = int(input())

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n + 1):
  if (i - 1) >= 0 and dp[i - 1]:
    dp[i] += 1
  if (i - 2) >= 0 and dp[i - 2]:
    dp[i] += 1
  if (i - 5) >= 0 and dp[i - 5]:
    dp[i] += 1
  if (i - 10) >= 0 and dp[i - 10]:
    dp[i] += 1

print(dp[n])
print(dp)
