import os
from PIL import Image

filename = 'C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\smolball.png'
ironman = Image.open(filename, 'r')
filename1 = 'C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\kas3.jpg'
bg = Image.open(filename1, 'r')
text_img = Image.new('RGBA', (800,600), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
text_img.paste(ironman, (0,0), mask=ironman)
text_img.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\test.png", format="png")