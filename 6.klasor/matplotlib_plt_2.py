import matplotlib.pyplot as plt
import numpy as np
# N=5
# x=np.linspace(0,10,N) # sıfırdan ona kadar eşit aralıklarla beş tane sayı vericek
# y=x
# plt.plot(x,y,"o--")
# plt.axis("off")  # gırafikteki eksenleri siler
# plt.show()
x=[1,2,3,4,5]
plt.plot(x,[y**2 for y in x])
plt.axis("off")
plt.show()