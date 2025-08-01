a = 5
b = 10

dp = [0] * (b - a)
dp[0] = 1

for i in range(1, b - a):
  
  i1 = i - 1
  if i1 >= 0 and dp[i1] > 0:
    dp[i] += dp[i1]
  
  if (i+a) % 3 == 0:
    i3 = (i+a) // 3
    if i3 >= 0 and dp[i3] > 0:
      dp[i] += dp[i3]

print(dp)

print(dp[-1])
