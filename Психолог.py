from tkinter import *
import random
root = Tk()
root.title('Психолог')
root.geometry('500x330')
dictlist=['ты сказал мне','я говорю тебе','диагноз']
ansdict = ['Это здорово!','Это радует','Это огорчает','Всё будет хорошо!','Это здорово!','Это радует','Это огорчает','Всё будет хорошо!','Всё будет хорошо!']
def buttonclick1():
     Input.delete(0, 'end')
     Answer.config(text = '')
def buttonclick2():
     n = random.randint(0,9)
     Answer.config(text = ansdict[n])
def scaleValue(event):
    n=Slider.get()
    Answer.config(text=ansdict[n])
    

d = []
border = []

for i in range(3):
     d.append(Label(root, text = dictlist[i]))
     d[i].place(x = 20, y = 10+i*90,width = 460, height = 30)
     border.append(Frame(root, borderwidth=4,relief = 'groove'))
     border[i].place(x = 20, y = 40+i*90,width = 460, height = 50)

Input = Entry(border[0])
Input.place(x = 10,y = 10, width = 440,height = 30)
Answer = Label(border[1])
Answer.place(x = 10,y = 10, width = 440,height = 30)
Slider = Scale(border[2],orient = 'horizontal', command = scaleValue)
Slider.config(from_ = 0, to = 8,len=430, showvalue = 0)
Slider.pack(pady = 10)

Button1 = Button(root, text = 'Заново',command = buttonclick1)
Button2 = Button(root, text = 'Готово',command = buttonclick2)
Button1.place(x = 120, y = 285, width = 120, height = 30)
Button2.place(x = 250, y = 285, width = 120, height = 30)

root = mainloop()
