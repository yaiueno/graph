import numpy as np

mylist=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(mylist)
A = np.array(mylist)
print(A)
print(A.shape)
print(A[1,2])
print(A[-1,2])
print(A[0:2,1:])
print(A[0:2,1:2])