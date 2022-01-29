from tkinter import *
def take():
    l['text'] = "Выдано"

root = Tk()
Label(text="Пункт выдачи").pack()
Button(text = "Bзять", command=take).pack()
l = Label(width = 10, height = 1)
l.pack()
root.mainloop()
