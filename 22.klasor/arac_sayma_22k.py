import cv2
import numpy as np

vid = cv2.VideoCapture("4.2 traffic.avi.avi")

# Arka planı çıkarmak için MOG2 algoritması kullanılıyor
backsub = cv2.createBackgroundSubtractorMOG2()

# Geçen araç sayısını tutmak için sayaç
c = 0

while True:
    ret, frame = vid.read()
    
    if ret:
        # Arka plan çıkarma işlemi uygulanarak foreground (ön plan) maskesi elde edilir
        fgmask = backsub.apply(frame)

        # Araçları saymak için ekrana iki adet yeşil çizgi çizilir (kontrol alanı)
        cv2.line(frame, (50, 0), (50, 300), (0, 255, 0), 2)
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), 2)

        # Ön plan maskesi üzerinde konturlar (nesne sınırları) bulunur
        contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Hiyerarşiyi kontrol et
        try:
            hierarchy = hierarchy[0]
        except:
            hierarchy = []

        # Bulunan her kontur için işlem yapılır
        for contour, hier in zip(contours, hierarchy):
            (x, y, w, h) = cv2.boundingRect(contour)  # Konturun etrafına dikdörtgen oluştur
            if w > 40 and h > 40:  # Gürültüyü azaltmak için küçük konturlar göz ardı edilir
                # Aracı temsil eden dikdörtgeni çiz
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                
                # Dikdörtgen kontrol alanından (iki yeşil çizgi arası) geçerse araç sayısını artır
                if x > 50 and x < 70:
                    c += 1

        # Araç sayısı ekrana yazdırılır
        cv2.putText(frame, "car: " + str(c), (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Car Counting", frame)
        cv2.imshow("fgmask", fgmask)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()
