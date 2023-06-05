import pygame
from math import *
from random import randint

class Player(pygame.sprite.Sprite):
     def __init__(self, xPos=0, yPos=0):
          super().__init__()
          self.image = pygame.image.load('MarioSprites\gumba.png')
          self.x, self.y = xPos, yPos
          self.Bild = self.image
     def rotate(self, degree):
          self.Bild = pygame.transform.rotate(self.image, degree)
     def move(self, dist, xx, yy):
          self.x += xx
          self.y += yy
          dist -= 1
          return dist
     def  step(self, xx, yy):
          self.x += xx
          self.x += xx
     def destroy(self):
          self.image = pygame.image.load("MarioSprites\RIPgumba.gif")
          self.isKilled = True

Color = (0, 111, 111)
xMax, yMax = 600, 400
Direction = 0
degr = 0
dist = 0

pygame.init()
pygame.key.set_repeat(20, 20)
Window = pygame.display.set_mode((900, 700))                               
Figure = Player(xMax/2-50, yMax/2-50)

xStep = randint(0, 2)
if xStep == 0:
     xStep = -1
    
yStep = randint(0, 2)
if yStep == 0:
     yStep = -1

speedrunning = True
while speedrunning:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               speedrunning = False
          if event.type == pygame.MOUSEBUTTONDOWN:
               (xPos, yPos) = pygame.mouse.get_pos()
          if (xPos > Figure.x) and (xPos < Figure.x + 100) and (yPos > Figure.y) and (yPos < Figure.y + 100):
               Figure.destroy()
     if (Figure.x < 0) or (Figure.x > xMax - 110):
          xStep = -xStep
     if (Figure.y < 0) or (Figure.y > yMax - 110):
          yStep = -yStep
     
     degr = atan2(-yStep, xStep)
     degr = degrees(degr) - 90
     Figure.rotate(degr)

     Figure.step(xStep, yStep)
     pygame.time.delay(5)

     if not Figure.isKilled:
          Figure.step(xStep, yStep)
          pg.time.delay(5)
     
     Window.fill(Color)
     Window.blit(Figure.Bild, (Figure.x, Figure.y))
     pygame.display.update()

pygame.quit()
