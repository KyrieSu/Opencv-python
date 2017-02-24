import cv2
import numpy as np

img = cv2.imread('noise.jpg')
row , col , pix = img.shape
cv2.imshow('Original',img)
img0 = cv2.blur(img,(7,7))
cv2.imshow('Blur Smooth',img0)
img1 = cv2.medianBlur(img,5)
cv2.imshow('Median Smooth',img1)
img2 = cv2.GaussianBlur(img,(15,15),0)
cv2.imshow('Gaussian Smooth',img2)
img3 = cv2.bilateralFilter(img,9,36,36)
cv2.imshow('bilateral Smooth',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()