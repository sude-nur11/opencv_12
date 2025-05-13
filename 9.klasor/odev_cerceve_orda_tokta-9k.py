import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_black=np.array([80,161,120])
    upper_black=np.array([177,237,248]) #241,95,87 sayilari siyah renk için

    mask=cv2.inRange(hsv,lower_black,upper_black)
    
    _,th1=cv2.threshold(mask,150,200,cv2.THRESH_BINARY)
    edges = cv2.Canny(th1, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        cv2.drawContours(frame, [i],-1, (0, 255, 0), 3)  
        
        M = cv2.moments(i)
        if M["m00"] != 0:
           center_x = int(M["m10"] / M["m00"])
           center_y = int(M["m01"] / M["m00"])
            
           cv2.circle(frame, (center_x, center_y), 5, (255,0,0), -1)

    cv2.imshow('shapeFrame', frame)

    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



  