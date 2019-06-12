from tkinter import *


def slogan():
    print("Warning!!!")


root = Tk()


frame = Frame(root)
frame.pack()

b = Button(frame,
           text='QUIT',
           fg='RED',
           command=quit)

b.pack(side='left')

b1 = Button(frame,
            text='Hello',
            command=slogan)

b1.pack(side='right')

root.mainloop()
