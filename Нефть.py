from tkinter import *
from random import randint

Breadth = 500
Highness = 330

def button():
     l = ['red', 'orange', 'cyan', 'green', 'pink', 'gold', 'silver']
     for i in range(7):
          Graphic.create_oval(20, 20, Breadth-20-i * 10, Highness-20-i*10, fill = l[randint(0, len(l)) - 1])
          Graphic.create_oval(20, 20, Breadth-20-i * 10, Highness-20-i*10, fill = l[randint(0, len(l)) - 1])
root = Tk()
root.title = 'hello'
root.config(height = Highness, width = Breadth)
Graphic = Canvas(root, height = Highness, width = Breadth)
Graphic.pack()     
b = Button(root, text = 'посмотреть', command = button)
b.place(y = 30, x = 30)


root = mainloop()
