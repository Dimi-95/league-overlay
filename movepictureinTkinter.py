from tkinter import *
import os
from PIL import Image
import win32api, win32gui

#---------------------------------------

save = win32gui.FindWindow(None, "League of Legends (TM) Client")

(left, top, right, bottom) = win32gui.GetWindowRect(save)

position = (left, top, right, bottom)

print(position)

#----------------------------------------

root = Tk()
root.title("Dimi")
root.iconbitmap()
root.geometry(f"{right}x{bottom}+{left}+{top}")#(1927, 74, 3843, 785)
root.wm_attributes('-topmost', 1, '-transparentcolor', '#abcdef')
root.config(bg='#abcdef')
root.overrideredirect(1)

filename = 'C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\smolball.png'
ironman = Image.open(filename, 'r')
filename1 = 'C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\bg.png'
bg = Image.open(filename1, 'r')
text_img = Image.new('RGBA', (400,125), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
text_img.paste(ironman, (0,0), mask=ironman)
text_img.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\test.png", format="png")




t_img = PhotoImage(file="C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\test.png")

myimage = Label(image=t_img)
myimage.pack()


root.mainloop()