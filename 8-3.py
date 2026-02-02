import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,projection = "3d")

x = np.linspace(0, 3 * np.pi, 50)
y = np.linspace(0, 3 * np.pi , 50)

X,Y = np.meshgrid(x,y)
Z = np.cos(X) + np.sin(Y)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot_surface(X,Y,Z)
ax.contour(X,Y,Z,offset=Z.min())
plt.savefig('8-3.eps')

plt.show()