#Если n – число Фибоначчи, требуется вывести номер этого числа в последовательности. В противном случае требуется вывести -1

def task2(n):
  
  v1, v2 = 1,1
  vc = 0
  i = 2
  
  if n <= 0:
    return -1
  elif n == 1:
    return 2
  
  while True:
    vc = v1 + v2
    if vc > n:
      return -1
    elif vc == n:
      return i + 1
    i += 1
    v1,v2 = v2,vc

def task(n):
  if n <= 0:
    return -1
  elif n == 1:
    return 2
  
  dp = [0,1]
  i = 2
  while True:
    dp.append(dp[i-1] + dp[i-2])
    if dp[i] > n:
      return -1
    elif dp[i] == n:
      return i
    i += 1


n = int(input())
print(task2(n))
