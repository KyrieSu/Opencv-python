import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Taipei.jpg",0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([1200]),plt.yticks([100])
plt.show()
