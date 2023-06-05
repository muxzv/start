import pygame
from math import *

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
          
Color = (0, 111, 111)
xMax, yMax = 600, 400
Direction = 0
degr = 0
dist = 0
pygame.init()
pygame.key.set_repeat(20, 20)
Window = pygame.display.set_mode((900, 700))                               
Figure = Player(xMax/2-50, yMax/2-50)



speedrunning = True
while speedrunning:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               speedrunning = False

          if event.type == pygame.MOUSEBUTTONDOWN:
               (xPos, yPos) = pygame.mouse.get_pos()
               xDiff = xPos - Figure.x - 50
               yDiff = yPos - Figure.y - 50
               dist = sqrt(xDiff * xDiff + yDiff * yDiff)
               degr = atan2(-yDiff, xDiff)
               degr = degrees(degr) - 90
               xDiff /= dist
               yDiff /= dist
               Figure.rotate(degr)
     if dist > 5:
          dist = Figure.move(dist, xDiff, yDiff)
          pygame.time.delay(5)
     Window.fill(Color)
     Window.blit(Figure.Bild, (Figure.x, Figure.y))
     pygame.display.update()

pygame.quit()
