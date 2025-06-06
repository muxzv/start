# пробегаем всё время по +1
def Task1(x, y, n):
  for t in range(1000):
    if (t // x + t // y) >= n:
      return t
  return None
  
# моделируем по методу списка будущих событий
def Task2(x, y, n):
  t = 0 #текущее время
  
  c = 0 #кол-во напечатанных копий
  
  next_t_x = x # время, когда допечатается копия на первом принтере
  next_t_y = y # время, когда допечатается копия на втором принтере
  
  while c < n:
    if next_t_x == next_t_y:
      t = next_t_x
      c += 2
      print("Допечатывают оба принтера! Всего копий:", c)
      next_t_x += x
      next_t_y += y
    elif next_t_x < next_t_y:
      t = next_t_x
      c += 1
      print("Допечатывает X принтер! Всего копий:", c)
      next_t_x += x
    else:
      t = next_t_y
      c += 1
      print("Допечатывает Y принтер! Всего копий:", c)
      next_t_y += y

  return t


def checkMy(t, n, x, y):
  y_sum = t // y
  x_sum = t // x
  s = x_sum + y_sum
  return s >= n

# метод двоичного поиска по ответу (без учёта первой копии)
def TaskMyBisect(x,y,n):
  l = -1
  r = n * min(x, y) # правая граница - время, которого точно хватит. Как будто работает только один (самый быстрый) принтер
  
  while r - l > 1: # то есть между правым и левым что то есть
    mid = (l + r) // 2
    if checkMy(mid,n,x,y):
      r = mid
    else:
      l = mid
  return r

def checkTinkoff(t, n, x, y):
  t = t - min(x, y)
  return t // x + t // y >= n - 1

# метод двоичного поиска по ответу (с учётом первой копии сразу)
def TaskTinkoff(x,y,n):
  left = -1
  right = n * min(x, y) # правая граница - время, которого точно хватит. Как будто работает только один (самый быстрый) принтер
  
  while right - left > 1:
    mid = (left + right) // 2
    if checkTinkoff(mid, n, x, y):
      right = mid
    else:
      left = mid
  return right

# метод двоичного поиска по ответу (с отдельным учётом первой копии)
def TaskMyFinal(x,y,n):
  if n <= 0:
    return 0
  t_copy1 = min(x,y) # время на первую копию. учитываем, что второй принтер с самого начала не может работать, тк нету второго экземпяра, поэтому сначала один принтер (более быстрый) занят печатью первой копии
  if n == 1:
    return t_copy1
  without1 = TaskMyBisect(x,y,n-1) # учитываем, что одну копию уже сделали
  return t_copy1 + without1

# n - кол-во копий (не учитывая оригинала)

x, y, n = 2, 3, 8 #int(input("Скорость X принтера: ")), int(input("Скорость Y принтера: ")), int(input("Количество копий: "))

print('без учёта первой копии', Task1(x,y,n), Task2(x,y,n), TaskMyBisect(x,y,n))
print('с учётом первой копии', TaskTinkoff(x,y,n), TaskMyFinal(x,y,n))
