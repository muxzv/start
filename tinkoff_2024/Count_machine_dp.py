a = 2
b = 10

dp = [0] * (b-a+1)
dp[0] = 1

for i in range(1, b-a+1):
  
  if i > 0:
    dp[i] += dp[i-1]
  
  n = i + a # восстанавливаем текущее число
  
  if n % 3 == 0:
    n3 = n // 3 # новое число
    if n3-a >= 0: # индекс нового числа
      dp[i] += dp[n3-a]

print(dp)

print(dp[-1])
