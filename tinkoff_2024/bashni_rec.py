#задача про ханойские башенки

#ищем вспомогательный палка
def hlep(z,x):
  l1=[]
  l1.append(z)
  l2 = []
  l2.append(x)
  t = ['a','b','c']
  res = set(t) - set(l1) - set(l2)
  return list(res)[0]

#основная (рекурсивная) функция
def bashni(f,t,c,d):
  if c == 1:
    d["moves"].append(f"{f} -> {t}")
    return
  v = hlep(f,t)
  bashni(f,v,c-1,d)
  bashni(f,t,1,d)
  bashni(v,t,c-1,d)

#запуск программы
d = dict()
d["moves"] = []
bashni('a','b',4,d)
print(d)
