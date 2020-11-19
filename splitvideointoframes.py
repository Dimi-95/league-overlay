import cv2

vidcap = cv2.VideoCapture("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test videos\\kas5.mp4")
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\saved frames\\frame%d.png" % count, image)
    success, image = vidcap.read()
    print("Read a new frame: ", success)
    count += 1

