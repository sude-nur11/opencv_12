import cv2

cap=cv2.VideoCapture(0)

filame="vidyoyu kaydedecek yerin adresi,vidyonun adı"
codec=cv2.VideoWriter_fourcc("W","M","V","2")
frameRate=30
resolution=(640,480)
videokaydetme=cv2.VideoWriter(filame,codec,frameRate,resolution)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    cv2.imshow("webcam",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindpws()



