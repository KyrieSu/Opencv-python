import numpy as np
import cv2

cap = cv2.VideoCapture('mv.mp4') # argument is camera or file

while(cap.isOpened()):
    # Capture frame-by-frame
    ret , frame = cap.read() # return T or F

    # Our operations on the frame come here
    res = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #BGR -> GRAY or HSV

    # Display the resulting frame
    cv2.imshow('frame',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
