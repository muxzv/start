from tkinter import *
root = Tk()

root.title('Приветствие')

l1 = Label(text = 'C++', font = 'Arial 39')
l2 = Label(text = 'Python', font = ('Comic Sans Ms', 24, 'bold'))
l3 = Label(text = 'Java', font = 'Arial 77')
l4 = Label(text = 'C#', font = 'Arial 67')

l1.config(bd = 40, bg = '#0000ff')
l2.config(bd = 60, bg = '#ffff00')
l3.config(bd = 70, bg = '#7d00ff')
l4.config(bd = 10, bg = '#00ff00')

l1.pack()
l2.pack()
l3.pack()
l4.pack()
root.mainloop()
