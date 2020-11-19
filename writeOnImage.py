from PIL import Image, ImageDraw, ImageFont
import os
 
# name of the file to save

fnt = ImageFont.truetype('arial.ttf', 15)
# create new image
image = Image.new(mode = "RGB", size = (200,70), color = "red")
draw = ImageDraw.Draw(image)
draw.text((10,10), "LOOOOOOOOL", font=fnt, fill=(255,255,0))
image.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\tests.png")

