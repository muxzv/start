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

def task_full_rec_helper(l,n,var):
  if n < 100:
    task_full_rec_helper(l + [1], n+1,var)
    task_full_rec_helper(l + [20], n+20,var)
    task_full_rec_helper(l + [30], n+30,var)
  elif n == 100:
    var.append(l)

# через рекурсию выбор всех вариантов и затем выбор из них лучшего
def task_full_rec2():
  var = []
  task_full_rec_helper([], 0,var)
  #print(len(var))
  
  best = None
  best_l = 101
  for l in var:
    if len(l) < best_l:
      best = l
      best_l = len(l)
  
  return best
  
print(task_full_rec2())

def task_full_rec3_helper(l,n,var):
  if n < 100:
    task_full_rec3_helper(l + [1], n+1, var)
    task_full_rec3_helper(l + [20], n+20, var)
    task_full_rec3_helper(l + [30], n+30, var)

    minn = 101
    min_l = []
    for l in var:
      if len(l) < minn:
        min_l = l
        minn = len(l)
    
    var.clear()
    var.append(min_l)
  elif n == 100:
    var.append(l)

# перебор всех вариантов через рекурсию и оптимизацией выбора лучшего варианта
def task_full_rec3():
  var = []
  task_full_rec3_helper([],0,var)
  return var[0]
  
print(task_full_rec3())

# здесь определяется жадность
def next_item(l,res,n):
  
  for e in l:
    if sum(res) + e <= n:
      return e
  
  return None

# если используем жадный алгоритм, то получаем неверный результат
# для этой задачи нужно использовать динамическое программирование
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
