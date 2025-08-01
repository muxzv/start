a = 20
b = 22

dp = [0] * b
dp[a] = 1

for i in range(a+1, b):
  
  i1 = i - 1
  if i1 >= a and dp[i1] > 0:
    dp[i] += dp[i1]
  
  if i % 3 == 0:
    i3 = i // 3
    if i3 >= a and dp[i3] > 0:
      dp[i] += dp[i3]

print(dp)

print(dp[-1])
