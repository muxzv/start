from random import randint

num = randint(0, 100)
c = 0

while True:
    print('Enter your number: ')
    
    try:
        num2 = int(input())
    except:
        print('Game stopped')
        break
    
    c += 1
    if num2 > num:
        print('Less --')
    elif num2 < num:
        print('More ++')
    else:
        print('Yay! The number is ', num, '. Tries: ', c, '.', sep = '')
        break
    print('Tries', c)
