import cv2
import numpy as np
import matplotlib.pyplot as plt


# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,1000,(50,2)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(50,1)).astype(np.float32)
# np.ravel() -> convert n-D to 1D
# Take Red families and plot them
red = trainData[responses.ravel()==0]
print red
plt.scatter(red[:,0],red[:,1],80,'r','^')

# Take Blue families and plot them
blue = trainData[responses.ravel()==1]
print blue
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

newcomer = np.random.randint(0,1000,(5,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 5)

print "result: " , results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist

plt.show()