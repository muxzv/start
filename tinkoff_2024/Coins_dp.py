n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2,n + 1):
    dp[i] = dp[i - 1]
    if i % 10 % 5 % 2 == 0 or i % 2 == 0 or i % 5 == 0 or i % 10 == 0:
        dp[i] += 1
print(dp[-1])
