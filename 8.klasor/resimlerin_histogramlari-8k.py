import cv2
import numpy as np
from matplotlib import pyplot as plt

img2=cv2.imread("helicopter-army-01.webp")
b,g,r=cv2.split(img2)
# img=np.zeros((500,500),np.uint8)
# cv2.rectangle(img,(40,60),(280,300),(255,255,255),-1)

# cv2.imshow("img",img)
cv2.imshow("img2",img2)

# plt.hist(img.ravel(),256,[0,256])
# plt.hist(img2.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])       #burdaki ravel fonksiyonu degerleri tek bir satıra dokmeye yarar
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()