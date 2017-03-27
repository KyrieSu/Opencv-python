import cv2
import numpy as np


img = cv2.imread('lena.jpg')
row , col , pix = img.shape
cv2.imshow('original',img)
zoom_x = 1.5
zoom_y = 1.2
NN_img = cv2.resize(img, None, fx = zoom_x, fy = zoom_y, interpolation = cv2.INTER_NEAREST)
cv2.imshow('NN',NN_img)
Linear_img = cv2.resize(img,(int(col*zoom_x),int(row*zoom_y)),interpolation=cv2.INTER_LINEAR)
cv2.imshow('Linear',Linear_img)
center = (int(col/2),int(row/2))
angel = int(raw_input('Enter a value to rotate : '))
M = cv2.getRotationMatrix2D(center,angel,1)
rotate = cv2.warpAffine(img,M,(row,col))
cv2.imshow('rotate',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
