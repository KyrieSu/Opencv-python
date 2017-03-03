import numpy as np
import cv2
from matplotlib import pyplot as plt

X = np.random.randint(150,190,(200,1)) # Height
Y = np.random.randint(50,100,(200,1)) # Weight
# Z = X(Height)+Y(Weight) = [Height,Weight]
Z = np.hstack((X,Y))
# convert to np.float32
Z = np.float32(Z)

# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
ret,label,center=cv2.kmeans(Z,5,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
print len(center)
# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
C = Z[label.ravel()==2]
D = Z[label.ravel()==3]
E = Z[label.ravel()==4]
# Plot the data
plt.scatter(A[:,0],A[:,1],c = 'b')
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'g')
plt.scatter(D[:,0],D[:,1],c = 'y')
plt.scatter(E[:,0],E[:,1],c = 'k')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'm', marker = '*')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()