import cv2
import numpy as np

cap=cv2.VideoCapture("4.2 dog.mp4.mp4")

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #simdi beyaz bir nesneyi takip edicegimizden renk aralıgını yazalim
    # sensitivity = 15  # hassasiyet degeri
    lower_white = np.array([0,0,0])  #===> hsv code for blue/red/green/white şeklinde ara yapabiliriz
    upper_white = np.array([50,20,255])

    mask=cv2.inRange(hsv,lower_white,upper_white)
    res = cv2.bitwise_and(frame,frame,mask=mask)# ozel kullanımdan dolayı frame iki defa yazılır

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
	

cv2.destroyAllWindows()