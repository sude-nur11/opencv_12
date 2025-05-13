import cv2
# import numpy as np

img=cv2.imread("dunya-haritasi-2.jpg")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#resmimizin istedigimiz pikselindeki rengine ulasalim
color=img[2000,1259]
print("color:",color)
#simdide error almamak icin resmin boyutlarını bulalım
dimension=img.shape
print("boyut:",dimension)   # çıktı===> (2576, 3864, 3)

#istedigim kordinattali blue rengini bulayın
blue=img[1300,2000,0]
print("blue:",blue)
#bu istedigimiz kordinatlardaki engi  item  kullanarakta bulabiliriz
blue1=img.item(1500,1500,0)
print("blue1:",blue1)
#seçtigimiz pikseldeki renk degerini degistirelim
img[1300,2000,0]=200
print("new blue:",img[1300,2000,0])
#simdide degistirmek istedigimiz rengi  itemset  ile degistirelim
img.itemset((1500,1500,0),150)
print("new blue1:",img[1500,1500,0])

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# b=0,g=1,r=2 renkler