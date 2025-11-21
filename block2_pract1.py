import cv2

image = cv2.imread('room.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gray', gray)
cv2.imshow('Blur', blur)
cv2.waitKey(0)
cv2.imwrite('room_copied.png', blur)