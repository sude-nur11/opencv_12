import cv2
import numpy as np

img=cv2.imread("helicopter-army-01.webp",0)

#burdaki 150,200 min ve max degerlerdir
ret,th1 = cv2.threshold(img,150,200,cv2.THRESH_BINARY) # burdaki ret degeri gerksiz bir degerdir onun yerine _ de kullanılır
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,51,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)

cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()