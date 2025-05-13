import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_black=np.array([0,0,0])
    upper_black=np.array([255,203,219]) #255,203,219 penbe rengi siliyor 

    mask=cv2.inRange(hsv,lower_black,upper_black)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

    
cap.release()
cv2.destroyAllWindows()    