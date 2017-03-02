import cv2
import numpy as np

img = cv2.imread('opencv_logo.png',0)
#img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print cimg.shape
'''
Finds circles in a grayscale image using the Hough transform.
#4(mindst) -> Minimum distance between the centers of the detected circles.
    If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one.
    If it is too large, some circles may be missed.

#5 -> In case of CV_HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller).
#6 -> In case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected.
    Circles, corresponding to the larger accumulator values, will be returned first.
'''
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
print circles[0] , len(circles[0])
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()