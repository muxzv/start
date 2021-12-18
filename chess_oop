def mod(x):
    if x > 0:
        return x
    else:
        return -x
        
class ChessFigure:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def check(self, x, y):
        return false
        
class King(ChessFigure):
    def __init__(self, x, y):
        ChessFigure.__init__(self, "Король", x, y)
    def __str__(self):
        return self.name + " " + str(self.x) + "," + str(self.y)
    def check(self, x, y):
        dx = mod(x - self.x)
        dy = mod(y - self.y)
        if dx == 0 and dy == 0:
                return None
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)

#f1 = King(1,1)
#print(f1)
#print(f1.check(2,2)) #True
#print(f1.check(2,4)) #False
#print(f1.check(1,2)) #True
#print(f1.check(1,1)) #None

f1 = King(2,2)
print(f1)
print(f1.check(1,1)) #
