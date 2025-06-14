def index_by_value(v,sdvig): # по значению находим индекс элемента в массиве подсчета
  return v - sdvig

def CountingSort(uns,min_v,max_v): # основная функция сортировки подсчетом
  
  sdvig = min_v # сдвиг (т.к. минимальный элемент отображается в индекс 0)
  count_v = max_v - min_v + 1 # кол-во элементов
  
  l = [0] * count_v # вспомогательный список / список подсчета
  
  # заполнение списка подсчета
  
  for e in uns: # смотрим, сколько каких элементов есть в неотсортированном списке
    l[index_by_value(e,sdvig)] += 1
  
  res = []
  
  # использование списка подсчета
  
  for v in range(min_v, max_v + 1): #пробегаемся по всем возможным элементам
    count = l[index_by_value(v,sdvig)]
    if count > 0: # добавляем элемент(ы) в отсортированный список, если они есть
      res += [v] * count

  return res # отсортированный список

s1 = input()
uns = list(map(ord, [c for c in s1]))

min_v = ord('a')
max_v = ord('z')

res_c = ''.join(list(map(chr, CountingSort(uns,min_v,max_v))))

print(res_c)
