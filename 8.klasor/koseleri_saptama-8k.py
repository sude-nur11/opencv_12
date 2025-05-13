import cv2
import numpy as np

img1=cv2.imread("15.2 contour.png.png ")
img2=cv2.imread("15.1 text.png.png ")

gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gr=np.float32(gray) #gray i dogrudan kullanamadıgımızdan float32 ile cevirmemeiz gerekti

corners=cv2.goodFeaturesToTrack(gr,50,0.01,10)
# yukarıda once etkilenen sonra kac koşe bulacagı,kalite degeri ve son olarakta koseler arasi minumum uzaklık

# simdide corners ları kullanabilmemiz için int turune cevirmemiz gerekiyor
cor=np.int0(corners)

for corner in cor:
    x,y=corner.ravel()    #burdaki ravel fonksiyonu degerleri tek bir satıra dokmeye yarar
    cv2.circle(img2,(x,y),2,(0,0,255),-1)

cv2.imshow("corner",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
