from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("ПАРЫ")

matches = [1,1,2,2,3,3,4,4,5,5,6,6]

random.shuffle(matches)

myframe = Frame(root)
myframe.pack(pady = 10)

count = 0
anslist = [ ]
ansdict = { }

def button_click(b, number):
     global count, anslist,ansdict
     if b['text'] == ' ' and count < 2:
          b['text'] = matches[number]
          anslist.append(number)
          ansdict[b]=matches[number]
          count += 1
     if len(anslist) == 2:
          if matches[anslist[0]] == matches[anslist[1]]:
               my_label.config(text = 'Ура', font = 50)
               for key in ansdict:
                    key['state'] = 'disabled'
               count = 0
               anslist = []
               ansdict = {}
          else:
               my_label.config(text = 'Ой!')
               count = 0
               anslist = []
               messagebox.showinfo('Letter!','Не верно')
               for key in ansdict:
                    key['text'] = ' '
               ansdict = {}
               

b0 = Button(myframe, text = ' ',font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b0,0))
b1 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b1,1))
b2 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b2,2))
b3 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b3,3))
b4 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b4,4))
b5 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b5,5))
b6 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b6,6))
b7 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b7,7))
b8 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b8,8))
b9 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b9,9))
b10 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b10,10))
b11 = Button(myframe, text = ' ' ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda: button_click(b11,11))


b0.grid(row = 0, column = 0)
b1.grid(row = 0, column = 1)
b2.grid(row = 0, column = 2)
b3.grid(row = 0, column = 3)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)
b7.grid(row = 1, column = 3)

b8.grid(row = 2, column = 0)
b9.grid(row = 2, column = 1)
b10.grid(row = 2, column = 2)
b11.grid(row = 2, column = 3)

my_label = Label(root, text = '')
my_label.pack()

root = mainloop()
