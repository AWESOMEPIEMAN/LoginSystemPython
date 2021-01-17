from tkinter import *
import sys

def command1(event):
    if entry1.get() == 'usman' and entry2.get() == 'usman123' or entry1.get() == 'test' and entry2.get() == 'pass':
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()
root = Tk()
top = Toplevel()

top.geometry('300x300')
top.title('Login Screen')
top.configure(background='white')
photo2 = PhotoImage(file='img.png')
photo = Label(top, image = photo2, bg = 'white')
lbl1 = Label(top, text='Username',font=('Helvetica',10))
entry1 = Entry(top)
lbl2 = Label(top, text='Password',font=('Helvetica',10))
entry2 = Entry(top,show="*")
button2 = Button(top,text='Cancel', command=lambda:command2())

entry2.bind('<Return>',command1)
lbl3 = Label(top,text='Made by Usman Hamid Email : usmanhamid4ad@gmail.com',font=('Helvetica',10))

photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

root.title('Main Login Screen')
root.configure(background='white')
root.geometry('880x660')

root.withdraw()
root.mainloop()
