#Крестики-Нолики

field = [['0','0', '0'],['0', '0', '0'],['0', '0', '0']]

x = '1'
o = '2'
win = 0
point = [0, 0]
cn = 0
def paintF(x, y, symbol, field): #Функция для закраски клетки в поле
    field[x][y] = symbol

def winP(symbol): #Функция для определения победителя
    if symbol == '1':
        print('Крестики победили!')
    else:
        print('Нолики победили!')

def winF(symbol): # Функция для проверки выигрыша
   #По горизонтали
    for i in field:
         if (not '0' in i) and (not o in i):
            print('Крестики победили!')
            win = 1
            break
    #По вертикали
    if field[0][0] == symbol and field[1][0] == symbol and field[2][0] == symbol:
      win = 1
      return True
    elif field[0][1] == symbol and field[1][1] == symbol and field[2][1] == symbol:
        win = 1
        return True
    elif field[0][2] == symbol and field[1][2] == symbol and field[2][2] == symbol:
        win = 1
        return True
   #По диагонали
    elif field[0][0] == symbol and field[1][1] == symbol and field[2][2] == symbol:
        win = 1
        return True
    elif field[2][0] == symbol and field[1][1] == symbol and field[0][2] == symbol:
        win = 1
        return True
    else:
        return False

def prntFi(f):
   for i in f:
      print(*i)

while True:
    prntFi(field)

    #Ввод координат крестиков
    print('Ход крестиков!')
    x = int(input('Введите X клетки: ')) - 1
    y = int(input('Введите Y клетки: ')) - 1
    #Ход
    paintF(x, y, 'X', field)
    if winF('X'):
        print('Крестики победили!')
        prntFi(field)
        break
    
    prntFi(field)
    
   #Ввод координат ноликов
    print('Ход ноликов!')
    x = int(input('Введите X клетки: ')) - 1
    y = int(input('Введите Y клетки: ')) - 1
    #Ход
    paintF(x, y, 'O', field)
    if winF('O'):
        print('Нолики победили!')
        prntFi(field)
        break

#TODO: сделать проверку корректного/некорректного X или Y .
