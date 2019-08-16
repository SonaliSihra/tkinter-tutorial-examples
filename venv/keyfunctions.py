from tkinter import *

field_value = "Field value to output"  # returned from another part of the code


# triggered off left button click on text_field
def copy_text_to_clipboard(event):
    field_value = event.widget.get("1.0", 'end-1c')  # get field value from event, but remove line return at end
    window.clipboard_clear()  # clear clipboard contents
    window.clipboard_append(field_value)  # append new value to clipbaord


window = Tk()
# setup frame and grid
frame = Frame(window)
frame.grid()

# setup our inline label and widget
Label(frame, text="Field Label").grid(row=0, column=0)
text_field = Text(frame, height=1, borderwidth=0)
text_field.insert(1.0, field_value)
text_field.grid(row=0, column=1)
# Bind left click on text widget to copy_text_to_clipboard() function
text_field.bind("<Button-1>", copy_text_to_clipboard)
window.mainloop()
