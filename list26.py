import numpy as np
import matplotlib.pyplot as plt
import random

deta_x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
deta_y = np.array([random.uniform(-10.0,35.0) for i in range (len(deta_x))])
plt.bar(deta_x, deta_y)
plt.xlabel('Month')
plt.ylabel('Temperature[deg.C]')
plt.title('Climete in Yonezawa')
plt.savefig('graph6.eps')

plt.show()