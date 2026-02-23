import cv2
# Imports the OpenCV library for image processing.
img = cv2.imread('images/image.jpeg', 0)
# Reads the image from the given path in grayscale mode (0 = grayscale), 1 - Color Image, -1 - Loads image as such including alpha channel.
cv2.imshow('Image', img)
# Displays the image in a window titled "Image".
cv2.waitKey(2000)
# Waits for 2000 milliseconds (2 seconds) before closing the window.
cv2.destroyAllWindows()
# Closes all OpenCV windows opened during the program.