from tkinter import *
import sys
import os
import gobject
import gst


root = Tk()
root.title("dimi")
root.wm_attributes('-transparentcolor', '#abcdef')
root.config(bg='#abcdef')
root.geometry('400x200')
#root.overrideredirect(1)

photo = PhotoImage(file='C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\kas.png')
Label(root, image=photo).place(x=50, y=50)

root.mainloop()