import matplotlib.pyplot as plt
import numpy as np 
x=plt.imread('adres bilgisi') #resmin adres bilgisi yazılarak gösterilir
print(x)

print("red channel: ",x[50,50,0]) # rgb--> r =0, g=1, b=2
print("green channel: ",x[50,50,1])
print("blue channel: ",x[50,50,2])
print("rgb channel value: ",x[50,50,:]) # burda hepssinin red green ve blue rengini gösterir