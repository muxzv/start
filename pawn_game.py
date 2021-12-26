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
        self.p = p
        self.name = name
        self.is_white = is_white
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
        
p = Point(5,1)
#print(p)
#print(p.x)

f = Pawn(p, False)
print(f)

l = f.EatFields()

for i in l:
    print(i)
