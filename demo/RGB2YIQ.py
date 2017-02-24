import cv2

img  = cv2.imread("123.jpg",1)
row , col , pix = img.shape

for i in range(row):
    for j in range(col): # BGR
        tmp = img[i][j][0]*.0114 + img[i][j][1] *0.587 + img[i][j][2]*0.299
        for k in range(pix):
            img[i][j][k] = tmp
cv2.imshow("Taipei",img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('Grey_Taipei.jpg', img)
cv2.destroyAllWindows()
