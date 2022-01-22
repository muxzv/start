from tkinter import *


def green():
    l1['text'] = ("Вы нажали на зелёную кнопку")
    l1.config(bg='green')


def yellow():
    l1['text'] = ("Вы нажали на жёлтую кнопку")
    l1.config(bg='yellow')


def red():
    l1['text'] = ("Вы нажали на красную кнопку")
    l1.config(bg='red')



root = Tk()


l1 = Label(text = 'Пока ничего не нажато', fg = 'black', bg = 'orange', font=("Arial 51", 26, "italic"))
b1 = Button(text='Красная', command=red, bg = 'red', font=("Courier", 36, "italic"))
b2 = Button(text='Жёлтая', command=yellow, bg = 'yellow', font=("Courier", 36, "italic"))
b3 = Button(text='Зелёная', command=green, bg = 'green', font=("Courier", 36, "italic"))
b4 = Button(text='Выход', command=quit, bg = 'purple', font=("Courier", 36, "italic"))


l1.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()


root.mainloop()