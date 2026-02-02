import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.0001)
y = np.array(x**3-12*x)

plt.plot(x,y)

for i in range(1,len(x)-1):
    if y[i] > y[i+1] and y[i] > y[i-1]:
        plt.plot( x[i], y[i],marker = "s", color='green')
    if y[i] < y[i+1] and y[i] < y[i-1]:
        plt.plot( x[i], y[i], marker = 'o', color = 'red')
plt.xscale('linear')
plt.yscale('linear')

plt.title('graph of x^3 - 12x')

plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("8-2.eps")

plt.show()