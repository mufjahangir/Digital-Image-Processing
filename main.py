import cv2
import numpy as np
print(cv2.__version__)
img = cv2.imread('images/image.jpeg', 0)
print(img.shape)
cv2.imshow('Image', img)
cv2.waitKey(1000)