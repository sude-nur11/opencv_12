import cv2

# Kamera ve yüz/gülümseme tanıma modellerini yükle
vid = cv2.VideoCapture(0)
smile_cascade = cv2.CascadeClassifier('4.2 smile.xml.xml')
face_cascade = cv2.CascadeClassifier('4.1 frontalface.xml.xml')

while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)  # Ayna efekti (yatay çevirme)
    
    # Yüz tespiti için griye çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 9)
    
    for (x, y, w, h) in faces:
        # Yüzü kırmızı dikdörtgenle işaretle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # Yüz bölgesini (ROI) al
        roi_gray = gray[y:y+h, x:x+w]  # Düzeltme: y,x sırası önemli
        roi_img = frame[y:y+h, x:x+w]
        
        # Gülümseme tespiti yap
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 9)
        for (ex, ey, ew, eh) in smiles:
            # Gülümsemeyi yeşil dikdörtgenle işaretle
            cv2.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('Yüz ve Gülümseme Tanıma', frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()