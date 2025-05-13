import cv2

# Trackbar için boş fonksiyon
def nothing(x):
    pass

# İlk görüntüyü yükle ve boyutlandır
img1 = cv2.imread("1.1 aircraft.jpg.jpg")
img1 = cv2.resize(img1, (640, 480))  # 640x480 piksel boyutuna getir

# İkinci görüntüyü yükle ve boyutlandır
img2 = cv2.imread("7.1 balls.jpg.jpg")
img2 = cv2.resize(img2, (640, 480))  # Aynı boyutta olmalı

# İki görüntüyü %50-%50 oranında karıştır (başlangıç değeri)
output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Pencere oluştur
windowName = "Transition Program"
cv2.namedWindow(windowName)

# Geçiş efekti için trackbar oluştur (0-1000 arası değer)
cv2.createTrackbar("Alpha-Beta", windowName, 0, 1000, nothing)

while True:
    cv2.imshow(windowName, output)  # Güncel görüntüyü göster
    
    # Trackbar değerini oku ve normalize et (0.0-1.0 aralığına)
    alpha = cv2.getTrackbarPos("Alpha-Beta", windowName)/1000
    beta = 1 - alpha  # Alpha ve beta toplamı 1 olmalı
    
    # Görüntüleri yeni ağırlıklarla karıştır
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    print(f"Ağırlıklar - Alpha: {alpha:.2f}, Beta: {beta:.2f}")
    
    # ESC tuşu ile çıkış (27 = ESC'nin ASCII kodu)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()