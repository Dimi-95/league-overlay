from PIL import Image

def convertToPNG():
    img = Image.open('C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\frame1.png')#image path and name
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\new.png", "PNG")#converted Image name
    print('Done')

convertToPNG()