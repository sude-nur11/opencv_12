import cv2
import numpy as np

img=cv2.imread("helicopter-army-01.webp",0)
row,col=img.shape

M=cv2.getRotationMatrix2D((col/2,row/2),180,2)
# burdaki parenteze once sütün sonra satır sonra kaç derce döndürüleceği sonrada ölçeyi girilir
# ölçek yakınlıgını temsil eder

dst=cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()