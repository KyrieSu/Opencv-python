import cv2

img = cv2.imread("Noise.jpg",1)
row , col , pix = img.shape
W = 5
cv2.imshow("Noise",img)
for i in range(2,row-2):
    for j in range(2,col-2):
        for k in range(pix):
            tmp = [
                img[i-2][j+2][k], img[i-1][j+2][k], img[i][j+2][k], img[i+1][j+2][k],img[i+1][j+2][k],
                img[i-2][j+1][k], img[i-1][j+1][k], img[i][j+1][k], img[i+1][j+1][k],img[i+1][j+1][k],
                img[i-2][j][k],img[i-1][j][k],img[i][j][k],img[i+1][j][k],img[i+2][j][k],
                img[i-2][j-1][k], img[i-1][j-1][k], img[i][j-1][k], img[i+1][j-1][k],img[i+2][j-1][k],
                img[i-2][j-2][k], img[i-1][j-2][k], img[i][j-2][k], img[i+1][j-2][k], img[i+2][j-2][k],
                ]
            color = img[i][j][k]
            for z in range(0,(W-1)**2):
                tmp.append(color)
            tmp.sort()
            M = len(tmp)/2 # middle of the list
            img[i][j][k] = tmp[M]
cv2.imshow("Decrease_Noise",img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("DecreaseNoise.jpg",img)
cv2.destroyAllWindows()
