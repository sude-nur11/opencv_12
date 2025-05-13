import cv2
import os



cap=cv2.VideoCapture(0) 

frame_count=0
kaydedilenler="ss-klasoruuu"

while True:
    
    ret,frame=cap.read() 
    frame=cv2.flip(frame,1) 
    cv2.rectangle(frame,(20,20),(600,450),(0,255,0),5)
    cv2.imshow('Webcam',frame)
    if cv2.waitKey(1) & 0xFF==ord('t'): 
        break
    if cv2.waitKey(1) & 0xFF==ord('s'):
        frame_count +=1
        p=os.path.join(kaydedilenler,f'frame_{frame_count}.PNG')
        cv2.imwrite(p,frame)
        print(f'{p} kaydedildi')
    
cap.release() 
cv2.destroyAllWindows()