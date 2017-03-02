import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

# '''
# Canny algorithm
# #1 -> src image
# #2 -> low threshold
# #3 -> high threshold
# if #2 < value < #3 , then check neighborhood whether is "sure edge", if not , discard
#   elif value > #3 , denote sure edge
#   else discard
# #4 -> size of Sobel operator
# '''
#
# lines = cv2.HoughLines(edges,1,np.pi/180,170)
# '''
# First parameter, Input image should be a binary image, so apply threshold or use canny edge detection before finding applying hough transform.
# Second and third parameters are rho and theta accuracies respectively.
# Fourth argument is the threshold, which means minimum vote it should get for it to be considered as a line.
# '''
# print len(lines),type(lines)
# print lines[3]
#
# for line in lines:
#     rho , theta = line[0,0] , line[0,1]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for line in lines:
    x1,y1,x2,y2 =  line[0,0],line[0,1],line[0,2],line[0,3]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)




cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()