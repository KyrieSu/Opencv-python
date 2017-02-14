import cv2

img = cv2.imread("Noise.jpg",1)
row , col , pix = img.shape
cv2.imshow("Noise",img)
for i in range(1,row-1):
    for j in range(1,col-1):
        for k in range(0,pix):
            tmp = [ img[i-1][j+1][k] , img[i][j+1][k],img[i+1][j+1][k],
                img[i - 1][j][k] , img[i][j][k] , img[i+1][j][k],
                img[i - 1][j - 1][k],img[i][j-1][k],img[i+1][j-1][k]
                ]
            tmp.sort()
            M = len(tmp)/2 # middle of the list
            img[i][j][k] = tmp[M]
cv2.imshow("Decrease_Noise",img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("DecreaseNoise.jpg",img)
cv2.destroyAllWindows()