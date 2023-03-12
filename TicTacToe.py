#Крестики-Нолики

field = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
num = 2
win_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
cursym = 'X'
winsym = None

def correct_num(num, field):
    return not(field[num] == 'X' or field[num] == 'O' or num < 0 or num > 8)

def paintP(num, symbol, field): #Функция для закраски клетки в поле
    field[num - 1] = symbol

def allF(field):
     for l in field:
          for j in l:
               if not(j == 'X' or j == 'O'):
                    return False
     return True

def winF(field, symbol): # Функция для проверки выигрыша
    #По диагонали
    for i in win_indexes:
        if field[i[0]]==symbol and field[i[1]]==symbol and field[i[2]]==symbol:
            return True
    return False

def prntFi(field):
   for i in range(0,9,3):
      print(field[i], field[i + 1], field[i + 2])

while True:
    prntFi(field)
    
    #Проверка ничьи
    if allF(field):
      print('Ничья!')
      break
    
    #Ввод координат
    if cursym == 'X':
      print('Ход крестиков!')
    else:
      print('Ход ноликов!')
    
    while True:
        num = input('Введите номер клетки: ')
        #Проверка на сдачу '?'
        if num == 'сдаюсь':
            win = 1
            winsym = True
            break
        
        if correct_num(int(num) - 1, field):
           break
       
    if win == None:
        paintP(int(num), cursym, field)
    
    if winsym != None:
        winsym = cursym
    #Проверка выигрыша 
    elif winF(field, cursym):
        winsym = cursym
     
    if cursym == 'X':
       print('Нолики победили!')
       prntFi(field)
       break
    else:
       print('Крестики победили!')
       prntFi(field)
       break
    
    if cursym == 'X':
      cursym = 'O'
    else:
      cursym = 'X'
    

#TODO: что нибудь сделать
