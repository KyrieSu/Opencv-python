import cv2
import numpy as np

def show(img):
    dst = cv2.resize(img,(800,600))
    cv2.imshow('show',dst)
    cv2.waitKey(0)
    cv2.destroyWindow('show')

src = cv2.imread('1.jpg')
img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ret , img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

k = np.ones((5,5),np.uint8)
img = cv2.erode(img,k,iterations = 10)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)


show(img)