import numpy as np
import matplotlib.pyplot as plt
deta = np.array([[0, 1.3320], [10, 1.3461], [20, 1.3613], [30, 1.3780], [40, 1.3961], [50, 1.4145], [60, 1.4353], [70, 1.4493]])
fact = np.zeros(4)
for i in range(len(deta)):
    fact[0] += deta[i][0] * deta[i][1]
    fact[1] += deta[i][0]
    fact[2] += deta[i][1]
    fact[3] += (deta[i][0])**2
alpha = ( len(deta)* fact[0] - fact[1]*fact[2])/(len(deta) * fact[3] - (fact[1])**2)
beta = (fact[3] * fact[2] - fact[1] * fact[0])/(len(deta) * fact[3] - fact[1] ** 2)

plt.scatter(deta[:,0], deta[:,1], s=25,marker='*',color='blue')

x = np.arange(0,80,1)
y = np.array(alpha * x + beta)

plt.plot(x,y,color='red')

plt.xlabel('$x$-axis')
plt.ylabel('$y$-axis')
plt.title('$graph of 8.1$')
plt.savefig('8-1.eps')

plt.show()
