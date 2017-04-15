import cv2
import numpy as np
from matplotlib import pyplot as plt

sobelx = np.array([ [-1,0,1],[-2,0,2],[-1,0,1] ],np.float)
sobely = np.transpose(sobelx)

image = cv2.imread('lena.jpg',0)
row , col = image.shape

x_img = np.zeros(image.shape)
y_img = np.zeros(image.shape)
res = np.zeros(image.shape)
# for i in range(1, row-1):
#     for j in range(1, col-1):
#         #Calculate gx and gy using Sobel (horizontal and vertical gradients)
#         gx = (sobelx[0][0] * image[i-1][j-1]) + (sobelx[0][1] * image[i-1][j]) + \
#              (sobelx[0][2] * image[i-1][j+1]) + (sobelx[1][0] * image[i][j-1]) + \
#              (sobelx[1][1] * image[i][j]) + (sobelx[1][2] * image[i][j+1]) + \
#              (sobelx[2][0] * image[i+1][j-1]) + (sobelx[2][1] * image[i+1][j]) + \
#              (sobelx[2][2] * image[i+1][j+1])

#         gy = (sobely[0][0] * image[i-1][j-1]) + (sobely[0][1] * image[i-1][j]) + \
#              (sobely[0][2] * image[i-1][j+1]) + (sobely[1][0] * image[i][j-1]) + \
#              (sobely[1][1] * image[i][j]) + (sobely[1][2] * image[i][j+1]) + \
#              (sobely[2][0] * image[i+1][j-1]) + (sobely[2][1] * image[i+1][j]) + \
#              (sobely[2][2] * image[i+1][j+1])

#         x_img[i-1][j-1] = gx
#         y_img[i-1][j-1] = gy

#         #Calculate the gradient magnitude
#         # g = np.absolute(gx) + np.absolute(gy)
#         g = np.sqrt(gx * gx + gy * gy)
#         res[i-1][j-1] = g

x_img = cv2.filter2D(image,-1,sobelx)
y_img = cv2.filter2D(image,-1,sobely)
res = cv2.addWeighted(x_img,0.5,y_img,0.5,0)
# res = np.sqrt(np.square(x_img)+np.square(y_img))
# res = res.astype(int)
edges = cv2.Canny(image,100,200)
cv2.imshow('Gx',x_img)
cv2.imshow('Gy',y_img)
cv2.imshow('G',res)
cv2.imshow('Canny',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()