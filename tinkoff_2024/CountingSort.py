# сортировка подсчетом

def index_by_value(v,sdvig): # по значению находим индекс элемента в массиве подсчета
  return v - sdvig

def CountingSort(uns,min_v,max_v): # основная функция сортировки подсчетом
  
  sdvig = min_v # сдвиг (т.к. минимальный элемент отображается в индекс 0)
  
  l = [0] * count_v # вспомогательный список / список подсчета
  
  # заполнение списка подсчета
  
  for e in uns: # смотрим, сколько каких элементов есть в неотсортированном списке
    l[index_by_value(e,sdvig)] = l[index_by_value(e,sdvig)] + 1
  
  res = []
  
  # использование списка подсчета
  
  for v in range(min_v, max_v + 1): #пробегаемся по всем возможным элементам
    if l[index_by_value(v,sdvig)] > 0: # добавляем элемент(ы) в отсортированный список, если они есть
      res = res + [v] * l[index_by_value(v,sdvig)]

  return res # отсортированный список
  
uns = [20,10,17,15] #map(int, input().split())
min_v = 10
max_v = 20

print(*CountingSort(uns,min_v,max_v))
