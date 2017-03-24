import cv2
import numpy as np

def NN(img,zoom_y,zoom_x):
    row , col , pix = img.shape
    y = int(row*zoom_y)
    x = int(col*zoom_x)
    dst = np.zeros([y,x,pix],np.uint8)
    for j in xrange(0,y):
        _j = int(j/zoom_y + 0.5)
        for i in xrange(0,x):
            _i = int(i/zoom_x+0.5)
            dst[j,i] = img[_j,_i]
    return dst

def bilinear(img,zoom_y,zoom_x):
    '''
    ref : http://monkeycoding.com/?p=524
    :param img:
    :param zoom_y:
    :param zoom_x:
    :return:
    '''
    row , col , pix = img.shape
    y = int(row * zoom_y)
    x = int(col * zoom_x)
    dst = np.zeros([y, x, pix], np.uint8)
    for j in xrange(0,y):
        _j = j/zoom_y
        j1 = int(_j-0.5)
        j2 = int(_j+0.5)
        for i in xrange(0,x):
            _i = i/zoom_x
            i1 = int(_i-0.5)
            i2 = int(_i+0.5)
            tmp1 = img[j1,i1]+(_i-i1)*(img[j1,i2]-img[j1,i1])
            tmp2 = img[j2,i1]+(_i-i1)*(img[j2,i2]-img[j2,i1])
            dst[j,i] = tmp1+(_j-j1)*(tmp2-tmp1)

    return dst

if __name__ == "__main__":
    img = cv2.imread('lena.jpg')
    cv2.imshow('original',img)
    zoom_row = 1
    zoom_col = 1
    nn_img = NN(img,zoom_row,zoom_col)
    cv2.imshow('NN',nn_img)
    linear_img = bilinear(img,zoom_row,zoom_col)
    cv2.imshow('Bilinear',linear_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()