import cv2
import numpy as np


def nothing(x):
    pass

# Webcam'den görüntü almak için VideoCapture nesnesi oluştur
# 0, varsayılan kamera anlamına gelir
cap = cv2.VideoCapture(0)

# Trackbar penceresini oluştur
cv2.namedWindow("Trackbar")

# HSV renk aralığı için trackbar'lar oluştur
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)  # Lower Hue (0-179)
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)  # Lower Saturation (0-255)
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)  # Lower Value (0-255)
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)  # Upper Hue (0-179)
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)  # Upper Saturation (0-255)
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)  # Upper Value (0-255)

while True:
    # Kameradan kare okuma
    ret, frame = cap.read()
    
    # Görüntüyü yatay olarak çevir (ayna efekti)
    frame = cv2.flip(frame, 1)
    
    # Görüntü boyutunu yeniden ayarla
    frame = cv2.resize(frame, (500, 350))
    
    # BGR'den HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Trackbar'lardan değerleri al
    lh = cv2.getTrackbarPos("LH", "Trackbar")
    ls = cv2.getTrackbarPos("LS", "Trackbar")
    lv = cv2.getTrackbarPos("LV", "Trackbar")
    uh = cv2.getTrackbarPos("UH", "Trackbar")
    us = cv2.getTrackbarPos("US", "Trackbar")
    uv = cv2.getTrackbarPos("UV", "Trackbar")

    # Alt ve üst sınırları belirle
    lower_blue = np.array([lh, ls, lv])
    upper_blue = np.array([uh, us, uv])

    # Belirtilen renk aralığı için maske oluştur
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Maskeyi orijinal görüntüye uygula
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    
    cv2.imshow("frame", frame) 
    cv2.imshow("mask", mask)        
    cv2.imshow("bitwise", bitwise) 

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()