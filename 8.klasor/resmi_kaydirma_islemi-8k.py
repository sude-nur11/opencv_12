import cv2
import numpy as np

img=cv2.imread("helicopter-army-01.webp",0) # burdaki 0 sayısı resmi siyah beyaz yapmayı saglar
row,col=img.shape # row ifaddesi satır  col ifadesi sütünu temsil eder
#650
#600      çıktı

M=np.float32([[1,0,20],[0,1,180]]) # once x sonrada y ekseni için yazdık

dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

