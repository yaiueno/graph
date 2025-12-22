import numpy as np

matA = np.array([[1,2,3],[4,5,6]])
matB = np.array([[7,8,9],[10,11,12]])
print(matA.shape)
print(matB.shape)
print(matA + matB)
print((matA+matB).shape)
print(3 * matA)
print(matA.T)
print(matA.shape)
print(matA.T.shape)
print(np.dot(matA.T,matB))