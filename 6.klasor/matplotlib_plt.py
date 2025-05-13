import matplotlib.pyplot as plt
import numpy as np
x=np.arange(5) # birden beşe kadaar sayılar üretir
y=x
plt.plot(x,y,"o--") # o  o-  o--
plt.plot(x,-y,"o")
plt.plot(-x,y)
plt.title("sude") # bu kısımda gırafiğimize isim verdik
plt.show()
