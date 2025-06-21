# Имеется неограниченное количество купюр стоимостью 1, 20 и 30 единиц. Найдите
# способ выдать сумму в 100 единиц как можно меньшим количеством купюр.

def task_full_rec(l,n):
  global minn
  if n < 100:
    task_full_rec(l + [1], n+1)
    task_full_rec(l + [20], n+20)
    task_full_rec(l + [30], n+30)
  elif n == 100:
    if len(l) < minn:
      minn = len(l)

minn = 1000
task_full_rec([], 0)
print(minn)

# здесь определяется жадность
def next_item(l,res,n):
  
  for e in l:
    if sum(res) + e <= n:
      return e
  
  return None


def task_greedy(n,l):
  res = [] # результирующий набор
  while True:
    e = next_item(l,res,n) #берем подходящий элемент и перекладываем в res
    if e == None: #если таковых нет, заканчиваем сборку
      break
    res.append(e)

  return res

l = [30,20,1]
n = 100

print(task_greedy(n,l))
