import numpy as np

A = np.array([1,2,3])
B = 2
print(A+B)
A =np.arange(24).reshape(2,3,4)
B = 8
print(A+B)
C=np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
D = A +C
print(A.shape)
print(A)
print(C.shape)
print(C)
print(D.shape)
print(D)