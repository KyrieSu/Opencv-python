import numpy as np
import cv2
import sys

def _thinningIter(img,n):
    M = np.zeros(img.shape, np.uint8)
    print M
    row , col = img.shape
    for y in xrange(1,row-1,1):
        for x in xrange(1,col-1,1):
            p1 = img[y-1][x-1]
            p2 = img[y-1][x]
            p3 = img[y-1][x+1]
            p4 = img[y][x-1]
            p6 = img[y][x+1]
            p7 = img[y+1][x-1]
            p8 = img[y+1][x]
            p9 = img[y+1][x+1]
            num = p1+p2+p3+p4+p6+p7+p8+p9
            chanege = (p1==0 and p2==1)+(p2==0 and p3==1)+(p3==0 and p6==1)+(p6==0 and p9==1)+(p9==0 and p8==1)+(p8==0 and p7==1)+(p7==0 and p4==1)
            if n==0:
                m1 = p2*p6*p8
                m2 = p2*p4*p6
            else:
                m1 = p4*p6*p8
                m2 = p2*p4*p8
            if m1==0 and m2==0 and chanege==1 and 2<=num<=6:
                img[y][x] = 1

    return (img & ~M)


def thinning(src):
    dst = src.copy() / 255
    prev = np.zeros(dst.shape[0:2],np.uint8)
    count = 0
    while count <=10:
        dst = _thinningIter(dst, 0)
        dst = _thinningIter(dst, 1)
        count +=1
        diff = np.absolute(dst-prev)
        if np.sum(diff)==0:
            break
    return dst * 255

if __name__ == "__main__":
    src = cv2.imread('github1.jpg')
    if src is None:
        sys.exit()
    g_src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret , b_src = cv2.threshold(g_src, 10, 255, cv2.THRESH_BINARY)
    res = thinning(b_src)
    cv2.imshow('Original',src)
    cv2.imshow('thinning',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()