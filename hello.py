from tkinter import *

root = Tk()

logo = PhotoImage(file="source.gif")

w1 = Label(root, image=logo).pack(side="right")

explanation = """I'm writing this to create a bigger screen for the text\nand to see how the tkinter is actually 
wrapping up the data with a function pack() """

w2 = Label(root,
           justify=LEFT,
           padx=10,
           text=explanation).pack(side="left")

root.mainloop()