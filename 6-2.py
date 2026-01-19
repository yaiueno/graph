import numpy as np
deta = np.array([[0, 1.3320], [10, 1.3461], [20, 1.3613], [30, 1.3780], [40, 1.3961], [50, 1.4145], [60, 1.4353], [70, 1.4493]])
fact = np.zeros(4)
for i in range(len(deta)):
    fact[0] += deta[i][0] * deta[i][1]
    fact[1] += deta[i][0]
    fact[2] += deta[i][1]
    fact[3] += (deta[i][0])**2
alpha = ( len(deta)* fact[0] - fact[1]*fact[2])/(len(deta) * fact[3] - (fact[1])**2)
beta = (fact[3] * fact[2] - fact[1] * fact[0])/(len(deta) * fact[3] - fact[1] ** 2)

print (f"y = {alpha} x + {beta}")