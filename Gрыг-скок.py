from tkiknter import *
import random
import time

class Ball:
     def __init__(self, canvas, paddle, color):
          self.canvas = canvas
          self.paddle = paddle
          self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
          self.canvas.move(self.id, 245, 100)
          starts = [-3, -2, -1, 1, 2, 3]
          random.shuffle(starts)
          self.x = starts[0]
          self.y = -3
          self.canvas_height = self.canvas.winfo_height()
          self.canvas_width = self.canvas.winfo_width()
          self.hit_botton = False
     def hit_paddle(self, pos):
          paddle_pos = self.canvas.coords(self.padde.id)
          if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
               if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    return True
          return False
     def draw(self):
          pos = self.canvas.coords(self.id)
          if pos[1] <= 0:
               self.y = 3
          elif pos[3]
          
