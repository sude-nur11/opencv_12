import numpy as np
x=np.array([[1,2,3],[4,5,6]],np.int16)
print(x)
print(x[0])
print(x[0,0])
print(x[0][0]) # print(x[0,0]) == print(x[0][0])
print('*************')
print(x[:,0]) # çıktı= [1 4] 0. sütünü çağırmış olduk
print(x[0,:]) # çıktı= [1 2 3]


