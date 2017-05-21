import cv2
import numpy as np
import math

def myGaussian(length,weight):
    kernel = np.zeros((length,length))
    r = length/2
    Euler = 1.0/(2.0 * math.pi * math.pow(weight,2))
    total = 0
    kernel_radius = range(-r,r+1)

    for y in kernel_radius:
        for x in kernel_radius:
            d = (x**2+y**2)/((weight**2)*2)
            kernel[y+r,x+r] = Euler*math.exp(-d)
            total += kernel[y+r,x+r]
    
    number = range(0,length)
    for y in number:
        for x in number:
            kernel[y,x] = kernel[y,x]*(1.0/total)
    
    return kernel

if __name__ == "__main__":
    img = cv2.imread('lena.jpg')
    cv2.imshow('Before',img)
    k = myGaussian(7,0.84089642)
    img = cv2.filter2D(img,-1,k)
    cv2.imshow('After',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()