# здесь определяется жадность
def next_item(heap):
  if len(heap) == 0:
    return None
  return heap[0]
 

def task(l):
  res = []
  heap = l.copy() # оставшиеся элементы
  heap.sort(key=lambda a: a[1]-a[0])

  while True:
    
    e = next_item(heap)
    
    if e == None:
      break
    
    res.append(e)
    heap.remove(e)
  return res

print(task([[1,3],[4,5]]))
