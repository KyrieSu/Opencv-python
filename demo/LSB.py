import cv2

img  = cv2.imread("Grey_Taipei.jpg")
row , col , pix = img.shape

#print img

for i in range(row):
    for j in range(col):
        for k in range(pix):
            if '{0:08b}'.format(img[i][j][k])[1] == '0':
                img[i][j][k] = 0
            else:
                img[i][j][k] = 255
img  = cv2.imshow("Digit",img)
cv2.waitKey(0)
print img