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
    def __init__(self):
        self.figures = []
    def fill_figures(self):
        self.figures = []
        for i in range(1, 9):
            p = Point(i, 1)
            f  = Pawn(p, True)
            self.figures.append(f)
        for i in range(1, 9):
            p = Point(i, 8)
            f  = Pawn(p, False)
            self.figures.append(f)
    def whites(self):
        l = []
        for f in self.figures:
            if f.is_white:
                l.append(f)
        return l
    def blacks(self):
        l = []
        for f in self.figures:
            if not f.is_white:
                l.append(f)
        return l
            
    def Show(self):
        # пробегаем по строкам
        for y in range(1,9):
            s = ''
            # пробегаем по клеткам
            for x in range(1,9):
                b = True
                # конкретная клетка
                # ищем, стоит ли на ней фигура
                for f in self.figures:
                    if f.p.x==x and f.p.y==y:
                        if f.is_white:
                            s += '1'
                        else:
                            s += '0'
                        b = False
                        break
                if b:
                    s += '.'
            print(s)
        
    def GoGame(self):
        self.fill_figures()
        
        self.Show()
        
        hod_color = True
        
        while True:
            
            if hod_color:
                hod = random.choice(self.whites())
                enemies = self.blacks()
            else:
                hod = random.choice(self.blacks())
                enemies = self.whites()
            #print(hod)
            #print()
            # проверим, можно ли съесть что-нибудь
            b = False
            for i in hod.EatFields():
                #print(i)
                for black in enemies:
                    if black.p.x == i.x and black.p.y == i.y:
                        hod.Go(Point(black.p.x, black.p.y))
                        self.figures.remove(black)
                        b = True
                        break
                if b:
                    break
            # если ничего не съели, то просто ходим
            if not b:
                b = True
                MoveFieldsv = hod.MoveFields()
                movepoint =  MoveFieldsv[0]
                for i in self.figures:
                    if i.p.x == movepoint.x and i.p.y == movepoint.y:
                        b = False
                        break
                if b:
                    hod.Go(movepoint)

            if b:
                self.Show()
                hod_color = not hod_color
            
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
