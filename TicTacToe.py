#Крестики-Нолики

field = ['1','2', '3', '4', '5', '6', '7', '8', '9']
num = 2
win_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def correct_num(num, field):
    if field[num - 1] == 'X' or field[num] == 'O' or 0 < num or num > 8:
        return False
    else:
        return True

def paintP(num, symbol, field): #Функция для закраски клетки в поле
    field[num - 1] = symbol

def winF(field, symbol): # Функция для проверки выигрыша
    #По диагонали
    for i in win_indexes:
        if field[i[0]]==symbol and field[i[1]]==symbol and field[i[2]]==symbol:
            return True
    return False
    
def prntFi(f):
   for i in range(0,9,3):
      print(field[i], field[i + 1], field[i + 2])

while True:
    prntFi(field)

    #Ввод координат крестиков
    print('Ход крестиков!')
    while not correct_num(num, field):
        num = int(input('Введите номер клетки: '))
    #Ход
    paintP(num, 'X', field)
    if winF(field, 'X'):
        print('Крестики победили!')
        prntFi(field)
        break
    
    prntFi(field)
    
   #Ввод координат ноликов
    print('Ход ноликов!')
    while not correct_num(num, field):
        num = int(input('Введите номер клетки: '))
    #Ход
    paintP(num, 'O', field)
    if winF(field, 'O'):
        print('Нолики победили!')
        prntFi(field)
        break

#TODO: сделать проверку корректного/некорректного номера клетки .
