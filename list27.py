import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,projection = "3d")

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X,Y = np.meshgrid(x,y)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot_surface(X,Y,X**2-Y**2)
plt.savefig('graph7.eps')

plt.show()