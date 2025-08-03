#80945
#21605

s = input()
a = []
for e in s:
  a.append(int(e))

dp = [1] * len(a)

nums = [b for b in range(1,31)]
for i in range(1,len(a)):
  if a[i - 1] > 0 and int(str(a[i - 1]) + str(a[i])) in nums:
    dp[i] += dp[i - 1]
  else:
    dp[i] = dp[i - 1]

print(dp)
