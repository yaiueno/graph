import numpy as np
matC=np.arange(24).reshape(2,3,4)
matC_tran=matC.transpose(0,2,1)
print(matC.shape)
print(matC)
print(matC_tran.shape)
print(matC_tran)