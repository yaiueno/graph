import numpy as np
import matplotlib.pyplot as plt

deta=[1,3,5,9,10,3,2,7,8,2]
plt.plot(deta)
plt.savefig('graph1.eps')
plt.show()

x = np.arange(-np.pi*2, np.pi*2,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.savefig('graph2.eps')
plt.show()

deta_x = np.arange(-3.2,3.4,0.2)
deta_y1 = [x**2 for x in deta_x]
plt.plot(deta_x, deta_y1, marker="s", color='red')
deta_y2 = 5.0*np.sin(deta_x)
plt.plot(deta_x, deta_y2,marker="o",color='blue')
plt.xlabel('$x$-axis')
plt.ylabel('$y$-axis')
plt.savefig("graph3.eps")

plt.show()
