import cv2

img = cv2.imread("Noise.jpg",1)
row , col , pix = img.shape
cv2.imshow("Noise",img)
for i in range(1,row-1):
    for j in range(1,col-1):
        tmp = [ img[i-1][j+1][0] , img[i][j+1][0],img[i+1][j+1][0],
                img[i - 1][j][0] , img[i][j][0] , img[i+1][j][0],
                img[i - 1][j - 1][0],img[i][j-1][0],img[i+1][j-1][0]
                ]
        tmp.sort()
        # M = len(tmp)/2 # middle of the list
        img[i][j][0] = tmp[4]
        img[i][j][1] = tmp[4]
        img[i][j][2] = tmp[4]
cv2.imshow("Decrease_Noise",img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("DecreaseNoise.jpg",img)
cv2.destroyAllWindows()