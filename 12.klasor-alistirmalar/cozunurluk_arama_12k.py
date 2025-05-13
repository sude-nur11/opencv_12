import cv2

# Pencere adını tanımla
windowName = "Live Video"
cv2.namedWindow(windowName)  # Video görüntüsü için pencere oluştur


cap = cv2.VideoCapture(0)  # 0 = varsayılan kamera

# Orijinal çözünürlüğü yazdır
print("Width : " + str(cap.get(3)))  # 3 = genişlik property ID'si
print("Height : " + str(cap.get(4)))  # 4 = yükseklik property ID'si

# Çözünürlüğü 1280x720 olarak ayarla
cap.set(3, 1280)  # Genişliği ayarla
cap.set(4, 720)   # Yüksekliği ayarla

# Yeni çözünürlüğü yazdır
print("Width* : " + str(cap.get(3)))
print("Height* : " + str(cap.get(4)))

# Ana video döngüsü
while True:
    _, frame = cap.read()  
    frame = cv2.flip(frame, 1)  # Yatay aynalama (1 = y eksenine göre)
    
    cv2.imshow(windowName, frame)
    
    # ESC tuşu ile çıkış (27 = ESC'nin ASCII kodu)
    if cv2.waitKey(1) == 27:
        break

cap.release() 
cv2.destroyAllWindows()  