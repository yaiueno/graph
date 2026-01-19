import numpy as np

evenarray = np.zeros(10)

for i in range(10):
    evenarray[i] = (i+1) * 2
print(evenarray)
msk = (evenarray % 4 == 0)
print (msk)
print (evenarray[msk])