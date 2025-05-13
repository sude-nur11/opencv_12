import cv2

cap = cv2.VideoCapture("4.2 line.mp4.mp4")

# Çizilecek dairelerin merkez noktalarını saklamak için liste
circles = []

# Fare olayları için callback fonksiyonu
def mouse(event, x, y, flags, params):
    # Sol fare tuşuna basıldığında
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))  # Tıklanan noktayı listeye ekle

# Pencere oluştur ve fare callback'ini ayarla
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

while True:
    # Videodan bir kare oku
    ret, frame = cap.read()
    
    # Video sonuna gelindiğinde döngüden çık
    if not ret:
        break
    
    # Kareyi yeniden boyutlandır
    frame = cv2.resize(frame, (640, 480))
    
    # Tüm daireleri çiz
    for center in circles:
        cv2.circle(frame, center, 20, (255, 0, 0), -1)  # Mavi, içi dolu daire
    
    # Görüntüyü göster
    cv2.imshow("Frame", frame)
    
    # Klavye girişini kontrol et
    key = cv2.waitKey(1)
    
    # ESC tuşu ile çıkış
    if key == 27:  # 27 = ESC'nin ASCII kodu
        break
    # 'h' tuşu ile tüm daireleri sil
    elif key == ord("h"):
        circles = []  # Daire listesini temizle

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()