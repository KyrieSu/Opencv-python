import cv2

img = cv2.imread('window.jpg',0)

print img.dtype
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print ret2

title = ['Original','Simple Threshold','Otsu']
window = [img , th1, th2]
for i in xrange(len(title)):
    cv2.imshow(title[i],window[i])
cv2.waitKey(0)
cv2.destroyAllWindows()