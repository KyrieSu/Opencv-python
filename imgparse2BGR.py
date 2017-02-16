import cv2
import numpy as np

img = cv2.imread('123.jpg',1) # 1 -> original mode ; 0 -> gray mode
img [:,:,0] = 0
img [:,:,1] = 0
cv2.imshow('RRRRRRRR',img)

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('R_Taipei.jpg', img)
cv2.destroyAllWindows()