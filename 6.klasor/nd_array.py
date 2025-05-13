import numpy as np
x=np.array([[-5,-1,3],[9,8,-10]],np.int16) # uint16 negatif sayılarla değil pozitif sayılarla çalısırım demek
print(x)
print(x.shape)
print(x.ndim)
print(x.dtype)
print(x.size) # eleman sayısı
print(x.T) # transpozon alır