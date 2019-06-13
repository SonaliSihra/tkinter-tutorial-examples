import tkinter as tk

from tkinter import messagebox


def click(event):
    if object_id is not None:
        coord = can.coords(object_id)
        width = coord[2] - coord[0]
        height = coord[3] - coord[1]

        can.coords(object_id, event.x, event.y, event.x + width, event.y + height)


def delete():
    msg = messagebox.askyesnocancel('Info', 'Delete canvas ?')
    if msg == True:
        can.delete(tk.ALL)


def create_circle():
    global object_id

    object_id = can.create_oval(10, 10, 70, 70, fill='orange', outline='blue')


# --- main ---

object_id = None

fenetre = tk.Tk()
fenetre.title('Dessin des objets')
fenetre.resizable(width=False, height=False)
fenetre.geometry('400x200+100+100')
fenetre.configure(bg='light green')

can = tk.Canvas(fenetre, bg='white', height=300, width=300)
can.pack(side=tk.RIGHT)
can.bind("<Button-1>", click)

btn_circle = tk.Button(fenetre, text='Circle', width=30, command=create_circle)
btn_circle.pack()

btn_delete = tk.Button(fenetre, text='Delete', width=30, command=delete)
btn_delete.pack()

fenetre.mainloop()
