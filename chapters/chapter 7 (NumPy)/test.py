import numpy as np
import numpy.matlib
#m = np.array([0,1,2,3,4,5,6,7,8,9,10])
# n = np.array([ input("give a number\n") for i in range(11)])

m = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
n = np.array([1,2,3,4,5,6,7,8,9,10])

#m = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

l = np.array(1)
print(np.array_split(m, 2))