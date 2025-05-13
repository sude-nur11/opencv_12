import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(x)
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]   üç boyutlu dizi çıktısı

'''
# elemanlarına ulaşalım
print(x[0,0,0])
# 11 sayısına ulaşmaya çalışalım
print(x[1,1,1]) 