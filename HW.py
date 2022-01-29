from tkinter import *
def red():
    l['text'] = 'красная'
def green():
    l['text'] = 'зелёная'
def yellow():
    l['text'] = 'жёлтая'
    
root = Tk()
root.title('ля-ля-ля')
l1 = Label(text = 'пока ничего не нажато').pack()
l = Label(width=10, heigh = 1)   
l.pack()
button1 = Button(text='кнопка1', bg = 'green', command = green).pack()
button2 = Button(text='кнопка2', bg = 'red', command = red).pack()
button3 = Button(text='кнопка3', bg = 'yellow', command = yellow).pack()

root = mainloop()
