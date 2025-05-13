import cv2

cap=cv2.VideoCapture("power.mp4")

while True:
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("heykel",frame)
    if ret==False:
        break
    if cv2.waitKey(20) & 0xFF== ord("q"):
        break
cap.release()
cv2.destroyAllWindows()    