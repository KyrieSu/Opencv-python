import cv2
import os
import random
import numpy as np

def check(img):
    # avoid exception
    if img is None:
        return False
    row , col , pix = img.shape
    # random 10 element to sample
    gray = np.array([128,128,128])
    H = 0
    while H<row:
        if np.array_equal(gray,img[H,0]):
            break;
        H+=1;
    if not np.array_equal(gray,img[H,:]):
        return False
    return True
    # for i in xrange(0,col-1,1):
    #     if not (np.array_equal(gray,img[H,i]) and np.array_equal(img[H,i],img[H,i+1])):
    #         return False
    # return True


if __name__ == "__main__":
    count = 0
    path = '/Volumes/Transcend/Opencv-python/272'
    for roots,dirs,files in os.walk(path):
        for f in files:
            print f
            img = cv2.imread(r'272/'+f,1)
            if check(img):
                print f
                # img = cv2.imshow('ERR',img)
                # cv2.waitKey(0)
                count+=1
                print count
            else:
                pass