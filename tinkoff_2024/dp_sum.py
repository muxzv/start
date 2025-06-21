# Имеется неограниченное количество купюр стоимостью 1, 20 и 30 единиц. Найдите
# способ выдать сумму в 100 единиц как можно меньшим количеством купюр.


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
