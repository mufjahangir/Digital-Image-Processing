import cv2
img = cv2.imread('images/image.jpeg', 0)
img = cv2.resize(img, (300, 400))

cv2.line(img, (50, 50), (200, 200), (255, 0, 0), 5)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.circle(img, (150, 150), 50, (0, 0, 255), -1)
cv2.ellipse(img, (150, 150), (50, 20), 0, 0, 360, (255, 255, 0), -1)
cv2.imshow('Shapes', img)

text = "Jahangir"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text, (50, 50), font, 1, (255, 255, 255), 2)
cv2.imshow('Shapes and Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
