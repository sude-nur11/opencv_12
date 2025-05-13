import cv2   


vid = cv2.VideoCapture('6.1 body.mp4.mp4')

body_cascade = cv2.CascadeClassifier("3.3 fullbody.xml.xml")

while 1:
    ret, frame = vid.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # yüzlerin koordinarlarını bulalım.
    bodies = body_cascade.detectMultiScale(gray)

    # yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

         
    cv2.imshow('video',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()