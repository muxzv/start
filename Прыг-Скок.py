from tkinter import *
import random
import time
cl = 'light cyan'

class Ball:
     def __init__(self, canvas, color):
          self.canvas = canvas
          self.id = canvas.create_oval(100, 100, 250, 250, fill = color)
          self.canvas.move(self.id, 245, 100)
          starts = [-3, -2, -1, 1, 2, 3]
          random.shuffle(starts)
          self.x = starts[0]
          self.y = random.randint(-3, 1)
          self.canvas_height = self.canvas.winfo_height()
          self.canvas_width = self.canvas.winfo_width()
     def draw(self):
          self.canvas.move(self.id, self.x, self.y)
          pos = self.canvas.coords(self.id)
          if pos[1] <= 0:
               self.y = 3
          elif pos[3] >= self.canvas_height:
               self.y = -3
          elif pos[0] <= 0:
               self.x = 3
          elif pos[2] >= self.canvas_width:
               self.x = -3
tk = Tk()
tk.title('Прыг-скок')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 1350, height = 700, bd = 0, bg = 'black', highlightthickness = 0)
canvas.pack()
tk.update()

ball1 =Ball(canvas, cl)
ball2 =Ball(canvas, cl)
ball3 =Ball(canvas, cl)

def draw_ball(ball):
     ball.draw()
     tk.update_idletasks()
     tk.update()
     time.sleep(0.01)

while 1:
     draw_ball(ball1)
     draw_ball(ball2)
     draw_ball(ball3)
