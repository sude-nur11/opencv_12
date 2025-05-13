import cv2
import numpy as np
import math

# Kontur listesinden en büyük alana sahip olanı bulan fonksiyon
def findMaxContour(contours):
    max_i = 0
    max_area = 0
    for i in range(len(contours)):
        area_hand = cv2.contourArea(contours[i])  # Mevcut konturun alanını hesapla
        
        if max_area < area_hand:  # Daha büyük alan bulunursa güncelle
            max_area = area_hand
            max_i = i
            
        try:
            c = contours[max_i]  # En büyük konturu seç
        except:
            contours = [0]  # Hata durumunda boş kontur oluştur
            c = contours[0]
        return c  # En büyük konturu döndür

# Kamera yakalama başlatılıyor
cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()  # Kameradan frame al
    frame = cv2.flip(frame, 1)  # Aynalama yap (y eksenine göre)
    
    # İlgi alanını (ROI) belirle [y1:y2, x1:x2]
    roi = frame[50:250, 200:400] 
    # ROI dikdörtgenini ana frame üzerine çiz
    cv2.rectangle(frame, (200,50), (400,250), (0,0,255), 0)

    # ROI'yi HSV renk uzayına çevir
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # Deri rengi için alt ve üst sınırlar
    lower_color = np.array([0,45,79], dtype=np.uint8)
    upper_color = np.array([17,255,255], dtype=np.uint8)

    # Maske oluştur (HSV aralığında kalan pikseller)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Gürültü azaltma ve maskeyi iyileştirme
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)  # Genişletme
    mask = cv2.medianBlur(mask, 15)  # Medyan filtreleme

    # Maskedeki konturları bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:  # Kontur bulunduysa
        c = findMaxContour(contours)  # En büyük konturu al
            
        # Konturun uç noktalarını bul:
        extLeft = tuple(c[c[:, :, 0].argmin()][0])  # En sol nokta
        extRight = tuple(c[c[:, :, 0].argmax()][0])  # En sağ nokta
        extTop = tuple(c[c[:, :, 1].argmin()][0])  # En üst nokta

        # Noktaları ROI üzerinde işaretle (yeşil daireler)
        cv2.circle(roi, extLeft, 5, (0,255,0), 2)
        cv2.circle(roi, extRight, 5, (0,255,0), 2)
        cv2.circle(roi, extTop, 5, (0,255,0), 2)

        # Noktalar arasında çizgiler çiz (mavi)
        cv2.line(roi, extLeft, extTop, (255,0,0), 2)
        cv2.line(roi, extTop, extRight, (255,0,0), 2)
        cv2.line(roi, extRight, extLeft, (255,0,0), 2)

        # Üçgenin kenar uzunluklarını hesapla (Pisagor)
        a = math.sqrt((extRight[0]-extTop[0])**2 + (extRight[1]-extTop[1])**2)
        c = math.sqrt((extTop[0]-extLeft[0])**2 + (extTop[1]-extLeft[1])**2)
        b = math.sqrt((extRight[0]-extLeft[0])**2 + (extRight[1]-extLeft[1])**2)

        try:
            # Kosinüs teoremi ile açıyı hesapla ve dereceye çevir
            angle_ab = int(math.acos((a**2 + b**2 - c**2)/(2*b*c)) * 57)
            # Açıyı ROI üzerine yazdır
            cv2.putText(roi, str(angle_ab), (extRight[0]-100+50, extRight[1]),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

            # Eğer açı 70°'den büyükse sol üstte mavi dikdörtgen göster
            if angle_ab > 70:
                cv2.rectangle(frame, (0,0), (100,100), (255,0,0), -1)
            
        except:  # Hesaplama hatası durumunda
            cv2.putText(roi, " ? ", (extRight[0]-100+50, extRight[1]),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
   
    
    cv2.imshow("frame", frame)
    cv2.imshow("roi", roi)
    cv2.imshow("mask", mask)

    # 'q' tuşu ile çıkış
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()