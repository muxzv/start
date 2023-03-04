#Крестики-Нолики

field = [['0','0', '0'],['0', '0', '0'],['0', '0', '0']]

x = '1'
o = '2'
win = 0
point = [0, 0] 

def prntF(f):
   for i in f:
      print(*i)

while True:
   prntF(field)

   #Ввод координат крестиков
   tpoint = x
   point = input('Ход крестиков! Введите координаты (через пробел)').split()
   field[int(point[1]) - 1][int(point[0]) - 1] = tpoint

   #Проверка выигрыша крестиков
   #По горизонтали
   for i in field:
         if (not '0' in i) and (not o in i):
            print('Крестики победили!')
            win = 1
            break
   #По вертикали
   if field[0][0] == x and field[1][0] == x and field[2][0] == x:
      win = 1
      print('Крестики победили!')
   if field[0][1] == x and field[1][1] == x and field[2][1] == x:
      win = 1
      print('Крестики победили!')
   if field[0][2] == x and field[1][2] == x and field[2][2] == x:
      win = 1
      print('Крестики победили!')
   #По диагонали
   if field[0][0] == x and field[1][1] == x and field[2][2] == x:
      win = 1
      print('Крестики победили!')
   if field[2][0] == x and field[1][1] == x and field[0][2] == x:
      win = 1
      print('Крестики победили!')
   
   if win == 1:
      prntF(field)
      break
   
   prntF(field)

   #Ввод координат ноликов
   tpoint = o
   point = input('Ход ноликов! Введите координаты (через пробел)').split()
   field[int(point[1]) - 1][int(point[0]) - 1] = tpoint

   #Проверка выигрыша ноликов
   #По горизонтали
   for i in field:
         if (not '0' in i) and (not x in i):
            print('Нолики победили!')
            win = 1
            break
   #По вертикали
   if field[0][0] == o and field[1][0] == o and field[2][0] == o:
      win = 1
      print('Нолики победили!')
   if field[0][1] == o and field[1][1] == o and field[2][1] == o:
      win = 1
      print('Нолики победили!')
   if field[0][2] == o and field[1][2] == o and field[2][2] == o:
      win = 1
      print('Нолики победили!')
   #По диагонали
   if field[0][0] == o and field[1][1] == o and field[2][2] == o:
      win = 1
      print('Крестики победили!')
   if field[2][0] == o and field[1][1] == o and field[0][2] == o:
      win = 1
      print('Крестики победили!')
   
   if win == 1:
      prntF(field)
      break

