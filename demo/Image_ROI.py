import cv2
import numpy as np

img = cv2.imread('123.jpg')
cv2.imshow('Original',img)
img1 = img[143:260,470:559]
# cv2.imshow('Test',img1)
img2 = img
row , col , pix =  img1.shape
x , y = img.shape[0] - row -1, 0
while (y+90) <= 600:
    img2[x:-1,y:y+col] = img1
    y = y + col
cv2.imshow('Test',img2)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('Ferris_Wheel.jpg', img1)
cv2.destroyAllWindows()