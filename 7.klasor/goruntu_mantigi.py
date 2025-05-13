import cv2
import numpy as np
img=np.zeros((10,10,3),np.uint8) # siyah beyaz cizimler yapicaksak kanalını 3 girmemize gerek yok
img[0,0]=(255,255,255) # beyaz
img[0,1]=(255,255,200) # asagi dogru koyu maviye gider
img[0,2]=(255,255,150)
img[0,3]=(255,255,15)


img=cv2.resize(img,(1000,1000),interpolation=cv2.INTER_AREA) # her bir pikseli bin kat büyüttük
cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()