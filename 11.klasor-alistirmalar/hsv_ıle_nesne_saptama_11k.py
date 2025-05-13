import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture("7.1 hsv.mp4.mp4")

cv2.namedWindow("Trackbar")
# HSV renk aralığı için alt (Lower) ve üst (Upper) sınırları ayarlamak üzere trackbar'lar oluşturuluyor
# Her bir trackbar, belirtilen pencereye ve aralığa göre ayarlanıyor
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing) 
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)  
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)  
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)

while 1:
    # Video karesini oku
    # `cap.read()` iki değer döndürür: başarı durumu (ret) ve kare (frame)
   
    _, frame = cap.read()
    
    frame=cv2.resize(frame,(640,480))

    # Kareyi BGR renk uzayından HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lardan alt (Lower) ve üst (Upper) HSV sınır değerlerini al
    lh = cv2.getTrackbarPos("LH", "Trackbar")
    ls = cv2.getTrackbarPos("LS", "Trackbar")  
    lv = cv2.getTrackbarPos("LV", "Trackbar")  
    uh = cv2.getTrackbarPos("UH", "Trackbar")
    us = cv2.getTrackbarPos("US", "Trackbar")  
    uv = cv2.getTrackbarPos("UV", "Trackbar") 
    
    # Trackbar'lardan alınan değerlerle alt ve üst sınırları oluştur
    lower_blue = np.array([lh, ls, lv])  # Alt HSV sınırları (Hue, Saturation, Value)
    upper_blue = np.array([uh, us, uv])  # Üst HSV sınırları

    # HSV görüntüsünde belirtilen aralıktaki renkleri maskele
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskeyi orijinal kareye uygula (sadece mavi renkli kısımları göster)
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri göster
    cv2.imshow("frame", frame)      # Orijinal kare
    cv2.imshow("mask", mask)   # Siyah-beyaz maske (beyaz: seçilen renk aralığı)
    cv2.imshow("bitwise", bitwise)  # Maskelenmiş sonuç

   
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()     