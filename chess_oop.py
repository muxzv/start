class ChessFigure:
    def __init__(self, name, x, y):
        self.name = name
        self.go(x, y)
    def __str__(self):
        return self.name + " " + str(self.x) + "," + str(self.y)
    def check(self, x, y):
        return False
    def go(self, x, y):
        self.x = x
        self.y = y

class King(ChessFigure):
    '''Король '''
    def __init__(self, x, y):
        ChessFigure.__init__(self, "Король", x, y)
    
    def check(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        if dx == 0 and dy == 0:
                return None
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

class Bishop(ChessFigure):
    ''' Слон '''
    def __init__(self, x, y):
        ChessFigure.__init__(self, "Слон", x, y)
    
    def check(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        if dx == 0 and dy == 0:
                return None
        return dx == dy

class Rook(ChessFigure):
    ''' Ладья '''
    def __init__(self, x, y):
        ChessFigure.__init__(self, "Ладья", x, y)
    
    def check(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        if dx == 0 and dy == 0:
                return None
        return dx == 0 or dy == 0

class Knight(ChessFigure):
    ''' Конь '''
    def __init__(self, x, y):
        ChessFigure.__init__(self, "Конь", x, y)
    
    def check(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        if dx == 0 and dy == 0:
                return None
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
        
class Queen(ChessFigure):
    ''' Ферзь '''
    def __init__(self, x, y):
        ChessFigure.__init__(self, "Ферзь", x, y)
    
    def check(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        if dx == 0 and dy == 0:
                return None
        return dx == 0 or dy == 0 or dx == dy
        
whites = list()
blacks = list()

whites.append(King(8,3))
blacks.append(King(5,5))

whites.append(Bishop(6,4))
blacks.append(Bishop(6,1))

whites.append(Rook(2,1))
blacks.append(Rook(8,4))

whites.append(Knight(4,6))
blacks.append(Knight(6,7))

whites.append(Queen(2,4))
blacks.append(Queen(3,4))

list1 = whites
list2 = blacks

o = True

while o:
    o = False
    
    for b in list1:
        for w in list2:
            if b.check(w.x, w.y):
                print(b, " ест ", w)
                b.go(w.x, w.y)
                list2.remove(w)
                o = True
                break
        if o:
            break
        
    list1,list2 = list2,list1
