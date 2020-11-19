import glob
from PIL import Image

images = glob.glob("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\saved frames\\*.jpg")
for image in images:
    with open(image, 'rb') as file:
        img = Image.open(file)
        img.show()
        