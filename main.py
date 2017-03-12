import cv2
import os
import numpy as np

def check(img):
    if img is None:
        return False
    row, col, pix = img.shape
    gray = np.array([128, 128, 128])
    H = row-1
    while H>=0:
        if np.array_equal(gray, img[H, 0]):
            break;
        H -= 1;
    if H==-1: # not find gray
        return False
    count = 0
    for i in xrange(col):
        if np.array_equal(img[H,i],gray):
            count += 1
            if count > (col/2):
                return True
    return False

if __name__ == "__main__":
    path = '/Volumes/Transcend/Opencv-python/user'
    for roots,dirs,files in os.walk(path):
        for dir in dirs:
            tmp_path = path + '/' + dir
            count = 0
            for roots,dirs,files in os.walk(tmp_path):
                for f in files:
                    img = cv2.imread(tmp_path + '/' + f)
                    if check(img):
                        count+=1
                        print f
                    else:
                        print "good:" , f
                print 'I am in ' + tmp_path + ' : ' , count