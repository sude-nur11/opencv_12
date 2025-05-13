import cv2
import numpy as np

img=cv2.imread("helicopter-army-01.webp",0)

kernel=np.ones((5,5),np.uint8)
erozyon=cv2.erode(img,kernel,iterations=5) #iterationu ve kernel degerini((5,5)) arttırırsak erozyon artar
di=cv2.dilate(img,kernel,iterations=5)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)#resimdeki gürültüyü kaldırır ve bozunmaya ugratır
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)#nesnenin içerisindeki bozulmaları düzeltir
gardient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("img",img)
# cv2.imshow("ero",erozyon)
# cv2.imshow("dilation",di)
# cv2.imshow("open",opening)
# cv2.imshow("close",closing)
# cv2.imshow("gari",gardient)
cv2.imshow("tophat",tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()