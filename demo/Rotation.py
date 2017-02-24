import cv2



img = cv2.imread('123.jpg',1)
rows,cols , pix  = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
'''
1st argument -> rotate center
2nd argument -> rotate angel
3nd argument -> zoom-in(out)
'''
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()