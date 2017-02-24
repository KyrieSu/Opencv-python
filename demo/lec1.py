import numpy as np
import cv2

img = cv2.imread('Taipei.jpg',0) # 1 -> original mode ; 0 -> gray mode
img1 = cv2.resize(img, (960, 540))
cv2.imshow('image',img1) # show image
res = cv2.waitKey(0) #forever wait
if res !=27: # 27 is ESC
    cv2.imwrite("Taipei101.jpg",img1)
cv2.destroyAllWindows()
