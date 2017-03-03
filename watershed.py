import cv2
import random
import numpy as np

img = cv2.imread('money.jpg',1)
row , col , pix = img.shape
cv2.imshow('Original',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# create binary image
ret , thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
cv2.imshow('Mask',thresh)
# using OPENING to remove inside noise
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
cv2.imshow('Opening',opening)

sure_bg = cv2.dilate(opening,kernel,iterations=3)
cv2.imshow('background',sure_bg)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
cv2.imshow('DistancrForm',dist_transform)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
cv2.imshow('frontground',sure_fg)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow('UNKNOWN',unknown)
# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
print ret
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
# if marker is -1 , then it will be border
img[markers == -1] = [0,255,0]
cv2.imshow('Finial',img)

cv2.waitKey(0)
cv2.destroyAllWindows()