import cv2
import os
import numpy as np

def makeBorder(img):
    img = cv2.dilate(img,(3,3),iterations=8)
    row , col = img.shape
    #img[:,0:90] = img[:,-80:-1] = 0
    img[0:90,:] = img[-100:-1,:] = 0
    return img

def show(img):
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img', 1200, 800)
    cv2.imshow('img', img)
    cv2.waitKey(0)


def travel(img):
    row , col = img.shape
    x = col/2
    for i in xrange(80,row,1):
        if img[i,x-1]==255 and img[i,x]==255 and img[i,x+1]==255:
            y = i
            break
    arr = []
    start = [y,x]
    tmp_y = y
    tmp_x = x
    arr.append(start)
    while arr and tmp_x<=col and tmp_y<=row:
        img[tmp_y,tmp_x] = 127
        if img[tmp_y,tmp_x+1]==255:
            arr.append([tmp_y, tmp_x + 1])
            tmp_x+=1
        elif img[tmp_y+1,tmp_x]==255:
            arr.append([tmp_y + 1, tmp_x])
            tmp_y+=1
        elif img[tmp_y,tmp_x-1]==255:
            arr.append([tmp_y, tmp_x-1])
            tmp_x-=1
        elif img[tmp_y-1,tmp_x]==255:
            arr.append([tmp_y-1, tmp_x])
            tmp_y-=1
        elif img[tmp_y,tmp_x+10]==255:
            arr.append([tmp_y,tmp_x+10])
            tmp_x+=10
        elif img[tmp_y+10,tmp_x]==255:
            arr.append([tmp_y+5,tmp_x])
            tmp_y+=10
        elif img[tmp_y,tmp_x-10]==255:
            arr.append([tmp_y,tmp_x-10])
            tmp_x-=10
        elif img[tmp_y-10,tmp_x]==255:
            arr.append([tmp_y-10,tmp_x])
            tmp_y-=10
        elif [tmp_y,tmp_x]==start:
            print 'Original'
            break
        else: #no way
            coords = arr.pop()
            tmp_y = coords[0]
            tmp_x = coords[1]
    return  img

def myRotate(img,src):
    '''
    ref: http://www.pyimagesearch.com/2017/02/20/text-skew-correction-opencv-python/
    :param img (binary image), src(original image):
    :return:
    '''
    coords = np.column_stack(np.where(img== 127))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    # otherwise, just take the inverse of the angle to make it positive
    else:
        angle = -angle
    print angle
    row , col , pix = src.shape
    center = (col/2,row/2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    res = cv2.warpAffine(src, M, (row-600,col+800),flags=cv2.INTER_LINEAR)
    return res


if __name__ == "__main__":
    path = r'1930_good'
    file = os.listdir(path)
    data = []
    readfile = open('file.txt','r')
    for filename in readfile:
        data.append(filename.split('\n')[0])
    for f in file:
        print f
        if f in data:
            continue
        src = cv2.imread(path+'\\'+f)
        name = f.split('.')[0]
        row , col , pix = src.shape
        middle_row = int(row/2)
        middle_col = int(col/2)
        gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        ret , binimg = cv2.threshold(gray,75,255,cv2.THRESH_BINARY_INV) # filter bg and fg
        offset = 30
        img1 = binimg[:,0:middle_col-offset]
        src1 = src[:,0:middle_col-offset]
        img2 = binimg[:,middle_col-offset:-1]
        src2 = src[:,middle_col-offset:-1]
        img1 = makeBorder(img1)
        img2 = makeBorder(img2)
        img1 = travel(img1)
        dst1 = myRotate(img1,src1)
        img2 = travel(img2)
        dst2 = myRotate(img2,src2)
        cv2.imwrite(r'myRotate\\'+name+'_1.jpg',dst1)
        cv2.imwrite(r'myRotate\\' + name + '_2.jpg', dst2)
        with open('file.txt','a') as writer:
            writer.write(f + '\n')
            writer.close()