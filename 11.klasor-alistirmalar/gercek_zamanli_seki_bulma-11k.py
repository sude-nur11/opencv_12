import cv2 
import numpy as np

# trackbar yapicagimiz için boş fonksiyon üretilim
def bos(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow("set")

cv2.createTrackbar("lower_Hue","set",0,180,bos)
cv2.createTrackbar("lower_saturation","set",0,255,bos)
cv2.createTrackbar("lower_value","set",0,255,bos)
cv2.createTrackbar("upper_Hue","set",0,180,bos)
cv2.createTrackbar("upper_saturation","set",0,255,bos)
cv2.createTrackbar("upper_value","set",0,255,bos)

font=cv2.FONT_HERSHEY_SIMPLEX

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #olustırdugumuz trackbarların pzisyonlarını alallım
    lh=cv2.getTrackbarPos("lower_Hue","set")
    ls=cv2.getTrackbarPos("lower_saturation","set")
    lv=cv2.getTrackbarPos("lower_value","set")
    uh=cv2.getTrackbarPos("upper_Hue","set")
    us=cv2.getTrackbarPos("upper_saturation","set")
    uv=cv2.getTrackbarPos("upper_value","set")
    # şimdi bu alınann pozisyonları maskta kullanabilmek için array oluşturalım

    lower_color=np.array([lh,ls,lv])
    upper_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_color,upper_color)
    # şimdide maska kernelı uyguluyarak beyaz renk üzerindeki siyah noktaları erozyona uğratalım
    kernel=cv2.once((5,5),np.uint8)
    mask=cv2.inRange(mask,kernel)
    # şimdide goruntunu kontorlarına ulaşalım
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # şimdide belli büyüklügün altındaki şekilleri tespit etmemesi için alan sınırlaması yapalım
    for cnt in contours:
        area=cv2.contourArea(cnt) # kontorların teker tekker alanlarını tespit ettik
        epsilon=0.02*cv2.arcLength(cnt,True)
        #şimdide approxla kontorları daha anlaşılır kılalım
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        # şeklin başlangıç kordimatlarına ulaşalim ve böylece şekin ismini yazıcagımız degere ulaşmış oluruz
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        # bell, bir alanın altındaki şekilleri yakalamaaması için alan sınırlaması belirleyelim
        if area > 400:
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            
            if len(approx)==3:
                cv2.putText(frame,"Triangle",(x,y),font,1,(0,0,0))
                
            elif len(approx)==4:
                cv2.putText(frame,"Rectangle",(x,y),font,1,(0,0,0))
                
            elif len(approx)>6:
                cv2.putText(frame,"Circle",(x,y),font,1,(0,0,0))
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    

    
   
