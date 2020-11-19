import cv2
import matplotlib.pyplot as plt 
import numpy as np

image = cv2.imread("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\kas2.jpg")

print("Image Type: ", type(image), 
      " Image Dimensions: ", image.shape)

image_copy = np.copy(image)

image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

lower_blue = np.array([0, 0, 100])
upper_blue = np.array([120, 100, 255])


mask = cv2.inRange(image_copy, lower_blue, upper_blue)
plt.imshow(mask, cmap="gray")


masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]

#plt.imshow(masked_image)

background_image = cv2.imread("C:\\Users\\Kas\\Desktop\\League overlay\\Overlay\\test images\\kas3.jpg")
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:1024, 0:1024]

crop_background[mask == 0] = [0, 0, 0]

#plt.imshow(crop_background)

final_image = crop_background + masked_image
plt.imshow(final_image)