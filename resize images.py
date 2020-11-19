import os
from datetime import datetime
from PIL import Image

for image_file_name in os.listdir('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Keystones'):
    if image_file_name.endswith(".png"):
        now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

        im = Image.open('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Keystones\\' +image_file_name)
        new_width  = 70
        new_height = 70
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        im.save('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\Runes\\Keystones2\\' + now + '.png')