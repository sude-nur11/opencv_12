import cv2
import numpy as np
tuval=np.zeros((512,512,3),dtype=np.uint8) +255  # çizim yaptıgımız icin int yerine unit kullanıyoruz
cv2.line(tuval,(50,30),(512,512),(255,0,0),thickness=5) # thickness kalınlık bildirir ama yazılmasına gerek yoktur 
cv2.line(tuval,(50,120),(512,512),(0,0,255),10)
cv2.rectangle(tuval,(50,50),(120,120),(0,255,0),8) #kare çizdirir (50,50)sol ust köşe (120,120)sag alt köşe  
# eger yapılan şeklin içerisini doldurmak istiyosak kalınlık kısmına -1 yazmalıyız
cv2.rectangle(tuval,(120,120),(240,240),(255,0,0),-1)
cv2.circle(tuval,(400,200),80,(0,0,255),5) # çember için önce merkez noktasını sonrada yarı çapını girdik
cv2.circle(tuval,(400,360),80,(0,0,255),-1)
# ucken cizmeye calışalım
cv2.line(tuval,(400,360),(500,460),(255,0,0),4)
cv2.line(tuval,(300,460),(500,460),(255,0,0),4)
cv2.line(tuval,(400,360),(300,460),(255,0,0),4)
#yamuk ya da çok gen cizimi
nokta=np.array([[20,350],[100,360],[10,444],[320,500]],np.int32)
cv2.polylines(tuval,[nokta],True,(0,0,100),8)    # noktalrı birlestirmesi için True yazılır
cv2.ellipse(tuval,(300,60),(100,40),20,0,360,(255,255,0),-1)
# merkez , yatay uzunluk ve dikey uzunluk , yatayla yaptığı açı(20), nerden nereye kadar kapsadığı , renk ve kalınlık


cv2.imshow("canvas",tuval) # hazırladığımız beyaz tuvalin ismi(canvas)
cv2.waitKey(0)
cv2.derstroyAllWindows()
'''(255,0,0)=mavi
   (0,255,0)=yeşil
   (0,0,255)=kırmızı 
'''