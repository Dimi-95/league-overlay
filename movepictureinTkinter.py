from tkinter import *
import os
from PIL import Image
import win32api, win32gui
from time import time


#------------find and store the | x,y and widthxheight | of a window---------------------------

save = win32gui.FindWindow(None, "League of Legends (TM) Client") #Finds the window - if it is online

(x, y, width, heigth) = win32gui.GetWindowRect(save) #saves the coordinates

position = (x, y, width, heigth) 

print(position)

#----------------------------------------

root = Tk()
root.title("Dimi")
root.iconbitmap() #the icon next to the label/title
root.geometry(f"{width}x{heigth}+{x-480}+{y+5}") 
root.wm_attributes('-topmost', 1, '-transparentcolor', '#abcdef') # topmost and the number next to it make sure that the window stays on top of other windows | transparentcolor make the window transparent
root.attributes("-alpha", 0.8)
root.config(bg='#abcdef')
root.overrideredirect(1) #removes the frame of the window, making it headless

#----------------- create a picture --------------------

#-------------BACKROUND-------------------------------
filename1 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\bg.png"
bg = Image.open(filename1, 'r')

#-------------KEYSTONE--------------------------------
filename2 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Keystones2\\Grasp.png"
keystone = Image.open(filename2, "r")

#-------------RUNES (1)-------------------------------
filename3 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\Rune_Absolute_Focus.png"
rune1 = Image.open(filename3, "r")

filename4 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\Rune_Gathering_Storm.png"
rune2 = Image.open(filename4, "r")

filename5 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\Celerity.png"
rune3 = Image.open(filename5, "r")

#-------------RUNES (2)-------------------------------
filename6 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\Font of Life.png"
rune4 = Image.open(filename6, "r")

filename7 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Runes2\\Second Wind.png"
rune5 = Image.open(filename7, "r")

#-------------SHARDS----------------------------------
filename8 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Rune Shards\\Rune_Adaptive_Force.png"
shard1 = Image.open(filename8, "r")

filename9 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Rune Shards\\Rune_Adaptive_Force.png"
shard2 = Image.open(filename9, "r")

filename10 = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Rune Shards\\Rune_Health.png"
shard3 = Image.open(filename10, "r")

#-------------PASTING OF PICTURES/COLLAGE-------------
text_img = Image.new('RGBA', (1117,62), (0, 0, 0, 0))
text_img.paste(bg, (0,0))

text_img.paste(keystone, (500, -10), mask=keystone )

text_img.paste(rune1, (600, 7), mask=rune1 )
text_img.paste(rune2, (655, 7), mask=rune2 )
text_img.paste(rune3, (710, 7), mask=rune3 )

text_img.paste(rune4, (790, 7), mask=rune4 )
text_img.paste(rune5, (845, 7), mask=rune5 )

text_img.paste(shard1, (925, 15), mask=shard1 )
text_img.paste(shard2, (965, 15), mask=shard2 )
text_img.paste(shard3, (1005, 15), mask=shard3 )




text_img.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\output.png", format="png")

#-------------------------------------------------------

#-------- take that picture and project it onto the transparent and headless window


t_img = PhotoImage(file="C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\output.png")

myimage = Label(image=t_img)
myimage.pack()

start = time()

root.after(7000, root.destroy)

root.mainloop()

 