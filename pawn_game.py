import random

class Point:
    '''
    Клетка на доске
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Figure:
    '''
    Шахматная фигура
    '''
    def __init__(self, p, name, is_white):
        self.name = name
        self.is_white = is_white
        self.Go(p)
    def __str__(self):
        if self.is_white:
            s = "Белая"
        else:
            s = "Чёрная"
        return s + " " + self.name + " координаты: " + self.p.__str__()
    def MoveFields(self):
        return []
    def EatFields(self):
        return []
    def Go(self, p):
        if hasattr(self,"p"):
            print(self.__str__() + " идёт на " + p.__str__())
        self.p = p

class Pawn(Figure):
    '''
    Пешка
    '''
    def __init__(self, p, is_white):
        Figure.__init__(self, p, "пешка", is_white)
    def MoveFields(self):
        l = []
        if self.is_white:
            l.append(Point(self.p.x, self.p.y + 1))
            return l
        else:
            l.append(Point(self.p.x, self.p.y - 1))
            return l 
    def EatFields(self):
        l = []
        if self.is_white:
            l.append(Point(self.p.x + 1, self.p.y + 1))
            l.append(Point(self.p.x - 1, self.p.y + 1))
        else:
            l.append(Point(self.p.x + 1, self.p.y - 1))
            l.append(Point(self.p.x - 1, self.p.y - 1)) 
        return l

class PawnGame:
    def Show(self, whites, blacks):
        # пробегаем по строкам
        for y in range(1,9):
            s = ''
            # пробегаем по клеткам
            for x in range(1,9):
                b = True
                # конкретная клетка
                # ищем, стоит ли на ней белая фигура
                for f in whites:
                    if f.p.x==x and f.p.y==y:
                        s += '1'
                        b = False
                        break
                if b:
                    # ищем, стоит ли на ней черная фигура
                    for f in blacks:
                        if f.p.x==x and f.p.y==y:
                            s += '0'
                            b = False
                            break
                if b:
                    s += '.'
            print(s)
        
    def GoGame(self):
        whites = []
        for i in range(1, 9):
            p = Point(i, 1)
            f  = Pawn(p, True)
            whites.append(f)
        
        blacks = []
        for i in range(1, 9):
            p = Point(i, 8)
            f  = Pawn(p, False)
            blacks.append(f)
        
        self.Show(whites, blacks)
        
        while True:
        
            hod = random.choice(whites)
            print(hod)
            print()
            # проверим, можно ли съесть что-нибудь
            b = False
            for i in hod.EatFields():
                print(i)
                for black in blacks:
                    if black.p.x == i.x and black.p.y == i.y:
                        hod.Go(Point(black.p.x, black.p.y))
                        blacks.remove(black)
                        b = True
                        break
                if b:
                    break
            # если ничего не съели, то просто ходим
            if not b:
                MoveFieldsv = hod.MoveFields()
                # TODO: проверить, не занята ли эта клетка
                movepoint =  MoveFieldsv[0]
                hod.Go(movepoint)
                
            self.Show(whites, blacks)
            
            if hod.is_white and hod.p.y >= 8:
                print('Белые выиграли!')
                break
            if not hod.is_white and hod.p.y <= 1:
                print('Чёрные выиграли!')
                break

        
game = PawnGame()
game.GoGame()

def Test():
    p = Point(5,1)
    #print(p)
    #print(p.x)
    
    f = Pawn(p, False)
    print(f)
    
    l = f.EatFields()
    
    for i in l:
        print(i)
    
    l = f.MoveFields()
    
    for i in l:
        print(i)
