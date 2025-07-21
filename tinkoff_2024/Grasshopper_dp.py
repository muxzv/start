l = list(map(int,input().split()))
n = l[0] #Его дом расположен рядом со столбиком номер n
k = l[1] #Кузнечик может прыгать вперед на любое количество столбиков от 1 до k

m = int(input()) #Количество сломавшихся столбиков 

if m > 0:
  ml = list(map(int,input().split())) # Номера сломавшихся столбиков
else:
  ml = []

dp = [0] * (n + 1) #элемент с индексом 0 не используется, индекс 1 - 1 столбик
dp[1] = 1
for e in ml:
  dp[e] = -1

for i in range(2,n + 1):
  if dp[i] == -1:
    continue
  
  for num in range(1,k + 1):
    if (i - num) >= 1 and dp[i - num] >= 1:
      dp[i] += dp[i - num]
      #print("Найден путь для ", i, 'палки, +', dp[i - num], 'путь')
  
print(dp[n])
