import numpy as np

x= np.array([[1.0,-0.5,3.5,-2.4],[-2.0,0.7,-4.5,+2.5],[0.6,-1.5,3.3,-4.4],[-1.5,5.5,-1.5,-8.4]])
print(x)

mask = (x <= 0)
print(mask)
x[mask] = 0
print(x)