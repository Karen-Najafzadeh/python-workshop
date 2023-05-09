import matplotlib.pyplot as plt
import numpy as np


#first plot
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2,3,1)
plt.plot(x,y)
plt.xlabel('fisrt plot x title')
plt.ylabel('fisrt plot y title')


# second plot
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2,3,5).grid()
plt.plot(x,y)
plt.xlabel('second plot x title')
plt.ylabel('second plot y title')


plt.suptitle('my subplot title')
plt.show()