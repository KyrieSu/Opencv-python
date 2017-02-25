import cv2
import numpy as np

img1 = cv2.imread('1.png',1) # BGR mode
img2 = cv2.imread('2.jpg',0) # gray mode
val = int(raw_input('Enter a value from each pixel : ')) #convert string to int

title = ['image1','image2']
img = [img1,img2]
for i in xrange(len(img)):
    cv2.namedWindow(title[i],cv2.WINDOW_NORMAL)
    cv2.imshow(title[i],img[i])

row,col,pix = img1.shape
H , W = img2.shape

# img1[:,:,:] = img1[:,:,:] - val;
# decrease value for each im img1
for i in xrange(row):
    for j in xrange(col):
        for k in xrange(pix):
            if img1[i][j][k] > val:
                img1[i][j][k] = img1[i][j][k] - val
            else:
                pass

#img2[:,:] = img2[:,:] - val
#decrease value for each in img2
for i in xrange(H):
    for j in xrange(W):
        if img2[i][j] > val:
            img2[i][j]= img2[i][j] - val
        else:
            pass

title = ['AFTER_image1','AFTER_image2']

for i in xrange(len(img)):
    cv2.namedWindow(title[i],cv2.WINDOW_NORMAL)
    cv2.imshow(title[i],img[i])
    cv2.imwrite(title[i]+'.jpg',img[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
