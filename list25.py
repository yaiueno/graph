import numpy as np
import matplotlib.pyplot as plt
import random
deta_x = np.array([random.uniform(0.0,10.0)for i in range(1000)])
deta_y = np.array([random.uniform(0.0,10.0)for i in range(1000)])
deta_radius = 5.0 * np.sqrt((deta_x)**2+(deta_y)**2)
plt.scatter(deta_x, deta_y, s=deta_radius)
plt.xlabel('$x$-axis')
plt.ylabel('$y$-axis')
plt.title('$r = x^2 + y^2$')
plt.savefig('graph5.eps')

plt.show()