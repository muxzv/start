from tkinter import *
from random import randint

Breadth = 500
Highness = 330

def button():
     for i in range(7):
          Graphic.create_oval(20, 20, Breadth-20-i * 10, Highness-20-i*10, fill = 'gold')
          Graphic.create_oval(20, 20, Breadth-20-i * 10, Highness-20-i*10, fill = 'gold')
root = Tk()
root.title = 'hello'
root.config(height = Highness, width = Breadth)
Graphic = Canvas(root, height = Highness, width = Breadth)
Graphic.pack()     
b = Button(root, text = 'БЛИНЫ БЕСПЛАТНО!!!!', command = button)
b.place(y = 30, x = 30)


root = mainloop()
