import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,projection = "3d")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

p=np.linspace(0,2*np.pi,50)
t=np.linspace(0,    np.pi, 50)
p,t = np.meshgrid(p,t)

X = np.sin(t)*np.cos(p)
Y = np.sin(t)*np.sin(p)
Z = np.cos(t)

ax.plot_surface(X,Y,Z)
plt.savefig('graph9.eps')

plt.show() 