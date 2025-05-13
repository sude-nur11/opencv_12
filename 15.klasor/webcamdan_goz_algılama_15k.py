import cv2 
  
vid = cv2.VideoCapture(0)

# Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("4.1 frontalface.xml.xml")
eye_cascade = cv2.CascadeClassifier("5.1 eye.xml.xml")

while 1:
    ret, frame = vid.read()
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(480,360)) #boyut belirtelim
    
    # kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # yüzlerin koordinarlarını bulalım.
    faces = face_cascade.detectMultiScale(gray)

    # yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # Şimdi de, bulduğum yüzler içinde göz arayacağım.
        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]

        # eye cascade dosyasını kullanarak gözlerin koordinatlarını bulalım.
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # bu koordinatlara dikdörtgen çizelim.
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
         
    cv2.imshow('video',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()