class ChessFigure:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def __str__(self):
        return self.name + " " + str(self.x) + "," + str(self.y)
    def check(self, x, y):
        return false


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
        
#f1 = King(1,1)
#print(f1)
#print(f1.check(2,2)) #True
#print(f1.check(2,4)) #False
#print(f1.check(1,2)) #True
#print(f1.check(1,1)) #None

f1 = King(2,2)
print(f1)
print(f1.check(1,1))

f2 = Bishop(4,3)
print(f2)
print(f2.check(6,5))

f3 = Rook(4,3)
print(f3)
print(f3.check(5,4))

f4 = Knight(4,3)
print(f4)
print(f4.check(5,5))

f5 = Queen(4,3)
print(f5)
print(f5.check(6,3))
print(f5.check(3,2))
print(f5.check(3,1))
