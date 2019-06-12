from tkinter import *

root = Tk()
root.title("Fav Language")

v = IntVar()

languages = [

    ("Python", 1),
    ("Java", 2),
    ("Perl", 3),
    ("C++", 4),
    ("C", 5)
]


def ShowChoice():
    print(v.get())


Label(root,
      text="""Choose your favorite programming language: """,
      justify=LEFT,
      padx=20).pack()

for val, language in enumerate(languages):
    Radiobutton(root,
                text=language,
                padx=20,
                variable=v,
                command=ShowChoice,
                value=val).pack(anchor=W)

root.mainloop()
