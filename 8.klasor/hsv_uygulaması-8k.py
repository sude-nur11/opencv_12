#bu uygulamada webcam den aldıgımız görüntüyü hsv ye ceviricez sonrada trackbarlarla da renk ayarları yapıcap
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def boss():
    pass

cv2.namedWindow("T-bar")
cv2.resizeWindow("T-bar",500,500) # bu kısımda bir pencere boyutlandırdıgımız için resizeWindow u kullandık

cv2.createTrackbar("lower H","T-bar",0,180,boss) 
cv2.createTrackbar("lower S","T-bar",0,255,boss)
cv2.createTrackbar("lower V","T-bar",0,255,boss)

cv2.createTrackbar("upper H","T-bar",0,180,boss) 
cv2.createTrackbar("upper S","T-bar",0,255,boss)
cv2.createTrackbar("upper V","T-bar",0,255,boss)

cv2.setTrackbarPos("upper H","T-bar",180)
cv2.setTrackbarPos("upper S","T-bar",255)
cv2.setTrackbarPos("upper V","T-bar",255)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    L_H=cv2.getTrackbarPos("lower H","T-bar")
    L_S=cv2.getTrackbarPos("lower S","T-bar")
    L_V=cv2.getTrackbarPos("lower V","T-bar")

    U_H=cv2.getTrackbarPos("upper H","T-bar")
    U_S=cv2.getTrackbarPos("upper S","T-bar")
    U_V=cv2.getTrackbarPos("upper V","T-bar")

    lower_color=np.array([L_H,L_S,L_V])
    upper_color=np.array([U_H,U_S,U_V])

    mask=cv2.inRange(frame_HSV,lower_color,upper_color) # yaptıklarımızın görüneceyi ekran bunuda inRange
                                                            #fonksuyonuyla yapıyoruz

    cv2.imshow("orijinal",frame)
    cv2.imshow("HSV",mask)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cv2.release()
cv2.destroyAllWindows()    