import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.001, 10, 0.1)
y = np.exp(2*x+1)

plt.plot(x, y)

plt.xscale('log')
plt.yscale('log')

plt.title('Double Logarithmic Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("graph4.eps")

plt.show()