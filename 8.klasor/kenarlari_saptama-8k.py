import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)  #ayna gibi

    edges=cv2.Canny(frame,100,200) # min ve max degerleri

    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()    
