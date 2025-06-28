def bashni1(f,t,c,d):
  d["moves"].append(f"{f} -> {t}")

def bashni2(f,t,c,d):
  v = hlep(f,t)
  bashni1(f,v,1,d)
  bashni1(f,t,1,d)
  bashni1(v,t,1,d)

def bashni3(f,t,c,d):
  v = hlep(f,t)
  bashni2(f,v,1,d)
  bashni1(f,t,1,d)
  bashni2(v,t,1,d)

def hlep(z,x):
  l1=[]
  l1.append(z)
  l2 = []
  l2.append(x)
  t = ['a','b','c']
  res = set(t) - set(l1) - set(l2)
  return list(res)[0]

d = dict()
d["moves"] = []
bashni3('a','b',3,d)
print(d)
