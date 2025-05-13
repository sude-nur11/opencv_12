#resimleri belirli yogunluklarda birbiri uzerine ekleme islemidir
#f(x,y)= x*a + y*b + c  olarak gosterilebilir

import cv2
import numpy as np

circle=np.zeros((512,512,3),np.uint8) + 255
cv2.circle(circle,(200,200),50,(0,255,0),-1)

rectangle=np.zeros((512,512,3),np.uint8) + 255
cv2.rectangle(rectangle,(100,100),(300,300),(255,0,0),-1)

dst=cv2.addWeighted(circle,0.6,rectangle,0.4,0) # burdaki 0 sabbit sayıdır yani c ile temsil edilen sayı

cv2.imshow("dst",dst)
cv2.imshow("kare",rectangle)
cv2.imshow("cember",circle)
cv2.waitKey(0)
cv2.destroyAllWindows()