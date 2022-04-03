from tkinter import *
import random

root = Tk()
root.title("ПАРЫ")

matches = [1,1,2,2,3,3,4,4,5,5,6,6]

random.shuffle(matches)

myframe = Frame(root)
myframe.pack(pady = 10)

count = 0
anslist = []
ansdict = {}

space = ''

buttons = []

def button_click(number):
     global count, anslist,ansdict
     b = buttons[number]
     if b['text'] == space and count < 2:
          b['text'] = matches[number]
     # if count > 2:
     #      count = 0
          #b0['text'] = space

for i in range(12):
     bi = Button(myframe, text = space ,font = ('Helvetica', 20), heigh = 3, width = 6,\
            command = lambda x=i: button_click(x))
     buttons.append(bi)

# b1 = Button(myframe, text =space ,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b1,1))
# b2 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b2,2))
# b3 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b3,3))
# b4 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b4,4))
# b5 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b5,5))
# b6 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b6,6))
# b7 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b7,7))
# b8 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b8,8))
# b9 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b9,9))
# b10 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b10,10))
# b11 = Button(myframe, text = space,font = ('Helvetica', 20), heigh = 3, width = 6,\
#             command = lambda: button_click(b11,11))

buttons[0].grid(row = 0, column = 0)
buttons[1].grid(row = 0, column = 1)
buttons[2].grid(row = 0, column = 2)
buttons[3].grid(row = 0, column = 3)

buttons[4].grid(row = 1, column = 0)
buttons[5].grid(row = 1, column = 1)
buttons[6].grid(row = 1, column = 2)
buttons[7].grid(row = 1, column = 3)

buttons[8].grid(row = 2, column = 0)
buttons[9].grid(row = 2, column = 1)
buttons[10].grid(row = 2, column = 2)
buttons[11].grid(row = 2, column = 3)

root = mainloop()
