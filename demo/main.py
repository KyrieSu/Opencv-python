import cv2
import os
import random
import numpy as np

def check(img):
    row , col , pix = img.shape
    buf = []
    # random 10 element to sample
    for i in xrange(10):
        buf.append(random.randint(0,col-1))
    color1 = img[-1,buf[0]] # the last row in image
    color2 = img[-1,buf[9]]
    if not (np.array_equal(color1,color2)):
        return True
    for i in xrange(1,len(buf)-1,1):
        if not (np.array_equal(img[-1,buf[i]],img[-1,buf[i+1]])):
            return True
    return False

if __name__ == "__main__":
    count = 0
    path = r'C:\Users\user\PycharmProjects\DEMO1\272'
    for roots,dirs,file in os.walk(path):
        for f in file:
            img = cv2.imread('272\\'+f,1)
            if not check(img):
                img = cv2.imshow('ERR',img)
                count+=1
                print f
            else:
                pass
    print count