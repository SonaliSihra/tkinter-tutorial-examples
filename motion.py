from tkinter import *


def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return


master = Tk()
whatever_you_do = """Whatever you do will be insignificant, but it is very important that you do 
it.\n(Mahatma Gandhi)"""
msg = Message(master, text=whatever_you_do)
msg.config(bg='white', font=('calibre', 18, 'italic'))
msg.bind('<Motion>', motion)
msg.pack()
mainloop()
