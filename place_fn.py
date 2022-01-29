from tkinter import *
from random import randint
def f():
    button1['bg'] = 'black'
    button1.place(x = randint(5, 40, y = randint(5, 40)

roott = Tk()
roott.title = 'lalala'
button1 = Button(root, text = "OK", width = 10, height = 5, fg = "red", font = "Arial 14", command = f)
button1.pack()
button1.place(x = 11, y = 15)
roott.mainloop()
