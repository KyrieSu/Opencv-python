import cv2
import numpy as np
import sys


if __name__ == '__main__':
    filename = sys.argv[1]
    img = cv2.imread(filename,0)
    img = cv2.resize(img,(800,600))
    img = cv2.medianBlur(img,5)
    ret , cimg = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ret , img = cv2.threshold(img,ret-70,255,cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    img = cv2.dilate(img,kernel,iterations = 1)
    img = cv2.erode(img,kernel,iterations = 10)
    num , label , stats , centroid = cv2.connectedComponentsWithStats(img,4,cv2.CV_32S)
    print num
    cv2.imshow('test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    