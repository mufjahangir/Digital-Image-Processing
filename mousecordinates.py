import cv2

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Mouse double clicked at position: ({}, {})".format(x, y))
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow('Image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Mouse right clicked at position: ({}, {})".format(x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('Image', img)
img = cv2.imread('images/image.jpeg', 0)
img = cv2.resize(img, (300, 400))
cv2.imshow('Image', img)

cv2.setMouseCallback("Image", mouse_event)


cv2.waitKey(0)
cv2.destroyAllWindows()