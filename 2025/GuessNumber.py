# Число от 0 до 100

def findn(l,r):
  ask = (int(l) + int(r)) // 2
  print('Это число',ask,'?')
  ans = input()
  if ans == '=':
    print('Загаданное число:', ask)
  elif ans == '+':
    findn(ask + 1,r)
  elif ans == '-':
    findn(l,ask - 1)

findn(0,100)
