import cv2
import numpy as np
img = cv2.imread('images/image.jpeg', 1)
cv2.imshow('Image', img)
print(img.shape)
key = cv2.waitKey(0)
# Waits indefinitely until a key is pressed. 0 means wait forever.

if key == ord('d'):
#Checks whether the pressed key is 'd', ord('d') converts character 'd' into its ASCII integer value. If the pressed key matches 'd', the condition becomes True.
    cv2.imwrite('images/image_copy.jpeg', img)
    print("Image saved successfully.")

cv2.destroyAllWindows()

