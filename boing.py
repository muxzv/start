"""Boing v. 0.1 by MaxiGames"""

class Boing:
    def __init__(self, x, y):
        self.x = x
        self.y=y

    def right(self):
        self.x+=10
    
    def left(self):
        self.x-=10
    
    def up(self):
        self.y+=10
    
    def down(self):
        self.y-=10
    
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)
    
    def home(self):
        self.y=0
        self.x=0


ball1=Boing(13, 5)
ball2=Boing(60, 29)

print(ball1)
print(ball2)

print(" ")

ball1.up()
ball2.left()

print(ball1)
print(ball2)

print("")

ball1.home()
ball2.home()

print(ball1)
print(ball2)

# оценка 5+ (папа)