import cv2
import numpy

img = cv2.imread('1.jpg',0)
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()