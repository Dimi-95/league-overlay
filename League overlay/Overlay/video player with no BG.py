from tkinter import *
import imageio
from PIL import Image, ImageTk
def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return   

    bg = Image.new(image.mode, image.size, image.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

    im = Image.open("bord3.jpg")
    im = trim(im)
    im.show()

########### Main Program ############

root = Tk()
root.title('Video in a Frame')
#root.wm_attributes('-transparentcolor', '#abcdef')
root.config(bg='#abcdef')
root.geometry('1920x1080')
#root.overrideredirect(1)


f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
video_name = "C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test videos\\kas2.mp4"   #Image-path
video = imageio.get_reader(video_name)
delay = int(100 / video.get_meta_data()["fps"])
stream()

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

im = Image.open("bord3.jpg")
im = trim(im)
im.show()


root.mainloop()