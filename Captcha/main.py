import cv2
import numpy as np
from PIL import Image
import pytesseract

img = cv2.imread('pic/1.jpg',1)
row,col,pix = img.shape
img = cv2.resize(img,(col*2,row*2))
row = row*2
col = col*2
Gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# use otsu algorithm to get Binary picture
ret , thresh = cv2.threshold(Gray_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#remove outside noise
thresh[0:3,:] = 255
thresh[:,0:2] = 255
thresh[-3:-1,:]  = 255
thresh[:,-2:-1] = 255

# use closing -> remove outside noise
kernel = np.ones((3,3),np.int8)
closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
#use opening -> remove inside noise
kernel = np.ones((2,2),np.int8)
opening = cv2.morphologyEx(closing,cv2.MORPH_OPEN,kernel)

title = ['Original','Gray','Binary','Closing','Opening']
image = [img,Gray_img,thresh,closing,opening]


for i in xrange(len(image)):
    cv2.namedWindow(title[i],cv2.WINDOW_NORMAL)
    cv2.imshow(title[i],image[i])

cv2.imwrite('temp.jpg',opening)

print pytesseract.image_to_string(Image.open('temp.jpg'))
cv2.waitKey(0)
cv2.destroyAllWindows()
