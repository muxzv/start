from tkinter import *

click = 0

def clicks():
    global click
    click += 1
    root.title("click {}".format(clicks))
    


root = Tk()


b1 = Button(text='1', command = clicks).grid(row=1, column = 1)

b2 = Button(text='2', command = clicks).grid(row=1, column = 2)
b3 = Button(text='3', command = clicks).grid(row=1, column = 3)

b4 = Button(text='4', command = clicks).grid(row=2, column = 1)
b5 = Button(text='5', command = clicks).grid(row=2, column = 2)
b6 = Button(text='6', command = clicks).grid(row=2, column = 3)

b7 = Button(text='7', command = clicks).grid(row=3, column = 1)
b8 = Button(text='8', command = clicks).grid(row=3, column = 2)
b9 = Button(text='9', command = clicks).grid(row=3, column = 3)

root = mainloop()
