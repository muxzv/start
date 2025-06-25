# Имеется неограниченное количество купюр стоимостью 1, 20 и 30 единиц. Найдите
# способ выдать сумму в 100 единиц как можно меньшим количеством купюр.

# способ с динамическим программированием (самый быстрый)
def task_dp():
  a, b, c = 1, 20, 30 #номиналы монет
  
  dp = [None] * 101 # индекс - сумма монет, а значение - мин. кол-во монет для набора этой суммы
  dp[0] = 0

  for i in range(1, 101): #заполняем dp
    if i >= c: #ищем минимальный элемент среди 3 вариантов  
      dp[i] = min(dp[i-a], dp[i-b], dp[i-c])
    elif i >= b: #ищем минимальный элемент среди 2 вариантов
      dp[i] = min(dp[i-a], dp[i-b])
    else: #ищем минимальный элемент среди 1 вариантов
      dp[i] = dp[i-a]
    dp[i] += 1
  
  return dp[100]

print(task_dp()) #выводим минимальное кол-во монет для суммы 100


#  вызывается при обнаружении нового варианта
def new_variant_detected(v,global_d):
  old_lenght = global_d['len']
  new_length = len(v)
  global_d['count'] += 1
  if (new_length < old_lenght):
    global_d['len'] = new_length
    global_d['variant'] = v
    
def task_full_rec4_helper(l,n,global_d):
  
  if n < 100:
    task_full_rec4_helper(l + [1], n+1,global_d)
    task_full_rec4_helper(l + [20], n+20,global_d)
    task_full_rec4_helper(l + [30], n+30,global_d)

  elif n == 100:
    new_variant_detected(l,global_d)

# рекурсия с вспомогательной функцией фиксации вариантов
def task_full_rec4():
  global_d = dict()
  global_d['len'] = 100
  global_d['variant'] = [1]*100
  global_d['count'] = 0
  task_full_rec4_helper([], 0, global_d)
  
  return global_d['variant']

print(task_full_rec4())


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
