#В доме у Саши работает очень странный лифт. В нем всего четыре кнопки: первые три позволяют подняться на 
#a,b и c этажей вверх соответственно, а последняя – спуститься на первый этаж.Требуется определить, сколько различных этажей доступно при помощи данного лифта.

n = int(input())

b = list(map(int,input().split()))
a,b,c = b[0],b[1],b[2]

dp = [False] * (n + 1)
dp[1] = True

co = 0

for i in range(2,n + 1):
  if (i - a) >= 0 and dp[i - a]:
    dp[i] = True
    co += 1
  elif (i - b) >= 0 and dp[i - b]:
    dp[i] = True
    co += 1
  elif (i - c) >= 0 and dp[i - c]:
    dp[i] = True
    co += 1
  
  #print(i,dp[i])

print(co + 1)
