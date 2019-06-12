from tkinter import *

counter = 0


def counter_label(label):
    def count():
        global counter
        counter += 2
        label.config(text=str(counter))
        label.after(1000, count)
        print("counter value: ", counter)

    count()


root = Tk()

root.title("counter!!")

label = Label(root, fg="green")

label.pack()

counter_label(label)
button = Button(root, text="Stop", width=25, command=root.destroy)
button.pack()

root.mainloop()