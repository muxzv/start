# > - больше
# < - меньше
# = - угадал

def Task(lowg_init, upg_init):

  f = True
  
  while f:
    lowg, upg = lowg_init, upg_init
    print('Загадайте число от', lowg, 'до', upg-1, 'включительно.')
    
    pred = -1
  
    while True:
      
      ask = (lowg + upg) // 2
      if not ask == pred:
        print(f'Это {ask}?')
        pred = ask
      else:
        print('Что-то пошло не так. Давайте попробуем ещё раз')
        pred = -1
        break
      
      ans = input()
      
      if ans == '>':
        lowg = ask
      elif ans == '<':
        upg = ask
      elif ans == '=':
        print('Число:',ask)
        f = False
        break

Task(1,5)
