# 21.11.2022 Программа "" Ход ладьи "". Цель: поставить ладю в точку 8 8. Ходить можно вверх или направо на любое кол-во клеток

from random import randint

def IsEnd(x, y):
    return x == 8 and y == 8

def Game(gamer1, gamer2):
    x, y = 1, 1
    print(x, y)
    
    gamer = 1
    
    while True:
        
        x, y = gamer1(x, y)
        print(x, y)
        if IsEnd(x, y):
            return gamer
        gamer = 3 - gamer
        
        x, y = gamer2(x, y)
        print(x, y)
        if IsEnd(x, y):
            return gamer
        gamer = 3 - gamer
        
def GetNextStep(x, y):
    print('Ваш ход: ')
    l = input().split()
    x = int(l[0])
    y = int(l[1])
    return x,y

def GetNextStepBot(x, y):
    if x > y:
        return x, x
    elif y > x:
        return y, y
    else:
        num = randint(0, 1)
        if num > 0:
            return x + randint(1, 8 - x), y
        else:
            return x, y + randint(1, 8 - y)

res = Game(GetNextStepBot, GetNextStep)

print('Выиграл игрок номер ', res)
