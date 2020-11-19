from PIL import Image

image = Image.open('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\kas4.jpg')


image_data = image.load()

height,width = image.size

for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]
        image_data[loop1,loop2] = r,30,b

image.save('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\changed.jpeg')