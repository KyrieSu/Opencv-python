import cv2
import random

img = cv2.imread("lena.jpg",1)
row , col , pix = img.shape
noiseRate = 0.06
for i in range(row):
    for j in range(col):
        if random.random() <= noiseRate: # random -> return float value
            for k in range(pix):
                img[i][j][k] = random.randint(1,255)
cv2.imshow("Add_Noise",img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("Noise.jpg",img)
cv2.destroyAllWindows()

