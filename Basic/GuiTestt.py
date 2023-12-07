import tkinter.messagebox
from tkinter import *


win=tkinter.Tk() #main window
win.title("Hewwo")
win.geometry('1024x640')

lab=Label(win,text='meow',width=20,height=10)
lab.pack()


def testbutt():
    tkinter.messagebox.showinfo("HEWWO MY FWEND","I'm not a cat")

btn = Button(win, text="CLICK", width=10, height=5, command=testbutt,)
btn.place(x=450, y=300)



can = Canvas(win, width=300, height=300, bg='red',)
oval=can.create_rectangle(10, 10, 290, 220, fill='purple')
can.pack()


win.mainloop() 