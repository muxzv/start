from random import randint

def randomint():
     num = randint(0, 100)
     return num

def PlayGame(num):
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
               print('Yay!')
               break

     print('Tries', c)

def end():
     print('The number is', num)


num = randomint()


randomint()
PlayGame(num)
end()
