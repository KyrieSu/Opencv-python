import cv2
import numpy as np

img1 = cv2.imread('yzu.png',1) # BGR mode
img2 = cv2.imread('yzu.png',0) # gray mode
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
            if img1[i,j,k] > val and img1[i,j,k]+val <= 255:
                img1[i,j,k] = img1[i,j,k] + val
            else:
                img1[i,j,k] = 255

#img2[:,:] = img2[:,:] - val
#decrease value for each in img2
for i in xrange(H):
    for j in xrange(W):
        if img2[i,j] > val and img2[i,j]+val <= 255:
            img2[i,j]= img2[i,j] + val
        else:
            img2[i,j] = 0

title = ['AFTER_image1','AFTER_image2']

for i in xrange(len(img)):
    cv2.namedWindow(title[i],cv2.WINDOW_NORMAL)
    cv2.imshow(title[i],img[i])
    cv2.imwrite(title[i]+'.jpg',img[i])
print 'success~'
cv2.waitKey(0)
cv2.destroyAllWindows()
