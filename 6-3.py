import numpy as np
rotarray = np.array([[np.cos(np.pi/4), 0, np.sin(np.pi/4)],
                     [0,1,0],
                     [-1 * np.sin(np.pi/4), 0, np.cos(np.pi/4)]])
vec = np.array([1/np.sqrt(2), 10, 1/np.sqrt(2)])
print(np.round(np.dot(rotarray,vec),5))