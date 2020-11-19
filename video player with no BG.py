import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test videos\\kas.mp4")
#cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    lower_green = np.array([30, 30, 0])
    upper_green = np.array([104, 153, 70])

    #mask =  cv2.inRange(hsv, lower_green, upper_green)

    cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

