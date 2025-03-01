def task_eratosphen(a, b):
  
  nums_list = [True for i in range(b+1)]
  
  
  sqr_a = b ** 0.5
  
  simple_set = list()
  
  if a in (1, 2) and b in (2, 3):
    simple_set.append(2)
  
  i = 2

  for i in range(2, int(b**0.5) + 1):
    if nums_list[i]:
      if i >= a:
        simple_set.append(i)
      for j in range(i*i, b+1, i):
          nums_list[j] = False

  for i in range(i+1, b+1):
    if nums_list[i]:
      if i >= a:
        simple_set.append(i)

  return simple_set


def test(a,b,res):
  r = task_eratosphen(a, b)
  if r != res:
    print('error:', a, b, r, res)

def run_tests():
  test(1,1, [])
  test(1,2, [2])
  test(2,2, [2])
  test(1,3, [2,3])
  test(3,3, [3])
  test(1,10, [2,3,5,7])
  test(5,7, [5,7])
  test(199,226, [199,211,223])
  
  print('end')
  
a,b = map(int,input().split())

simples = task_eratosphen(a,b)
if len(simples) == 0:
  print(-1)
else:
  for e in simples:
    print(e)
