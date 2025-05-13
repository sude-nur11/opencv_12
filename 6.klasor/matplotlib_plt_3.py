import matplotlib.pyplot as plt
import numpy as np
x= np.arange(3)
plt.plot(x,x**2)
plt.plot(x,5.2*x)
plt.legend(['x**2','5.2*x'],loc= 'upper right') #fonksiyonların her birine ayrı ad veririz   ***upper right/center/left,lower...
plt.grid(True) # grafik ızgarası oluşturur
plt.axis([0,2,0,10]) # x ve y nin max ve min değerlerini burda verdik
plt.xlabel('x= np.arange(3)')
plt.ylabel('y= f(x)')          # x ve y nin nerden geldiğini söyler
# plt.savefig('D:\\temp\\OpenCV\\plt.png') # parantez içerisine grafiğin kaydedileceği yerin adresi yazılır
plt.show()