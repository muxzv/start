from random import randint

num = randint(0, 100)
c = 0
num2 = -1

while True:
     print('Enter your number')
     num2 = input()
     c += 1
     if num2 == 'Exit':
          print('Game stopped')
          break
     elif  int(num2) > num:
          print('Less --')
     elif  int(num2) < num:
          print('More ++')
     else:
          print('Yay! The number is', num, '. Tries:', c)
          break
     print('Tries', c)
