import numpy as np
import cv2

cap = cv2.VideoCapture(0);
# create VideoWriter Obj to output Video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
'''
DIVX for windows,XVID is more preferable ,MJPG for high size video,X264 very small voido,WMV1,WMV2
'''
out = cv2.VideoWriter('test.avi',fourcc,20.0,(640,480))

while(cap.isOpened()): #check camera
    ret , frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break;

# release every process
cap.release()
out.release()
cv2.destroyAllWindows()
