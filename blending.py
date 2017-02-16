import cv2
import numpy as np

#  src1 and src2 must be have some size
img1 = cv2.imread('github1.jpg')
# print img1.shape
img2 = cv2.imread('git_logo.png')
# print img2.shape
dst = cv2.addWeighted(img1,0.2,img2,0.8,0)

cv2.imshow('Result',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()