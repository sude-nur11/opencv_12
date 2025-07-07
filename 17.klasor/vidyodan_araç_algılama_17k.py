import cv2

# Video ve cascade dosyalarını yükle
vid = cv2.VideoCapture("5.1 car.mp4.mp4")
car_cascade = cv2.CascadeClassifier("2.3 car.xml.xml")

while True:
    # Frame oku ve boyutlandır
    ret, frame = vid.read()
    if not ret: break  
    
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Arabaları tespit et
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)
    
    # Tespit edilen arabaları işaretle
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
    
    
    cv2.imshow("Araba Tespiti", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()