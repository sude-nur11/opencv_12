import cv2
import numpy as np
import math

# Kameradan video yakalamayı başlat
vid = cv2.VideoCapture(0)

while(1):
    try:  
        # Kameradan bir kare al
        ret, frame = vid.read()
        # Görüntüyü yatayda çevir (ayna efekti)
        frame = cv2.flip(frame, 1)
        
        # Görüntü işleme için çekirdek matrisi (3x3'lik bir matris)
        kernel = np.ones((3,3), np.uint8)
        
        # ROI (Region of Interest) - Elin konumlandırılacağı alan
        roi = frame[100:300, 100:300]
        
        # ROI'yi gösteren yeşil dikdörtgen çiz
        cv2.rectangle(frame, (100,100), (300,300), (0,255,0), 0)
        
        # ROI'yi HSV renk uzayına çevir
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        # Ten rengi için alt ve üst HSV sınırları
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        
        # Ten rengine göre maske oluştur
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        # Maskeyi genleştir (dilate)
        mask = cv2.dilate(mask, kernel, iterations=4)
        
        # Maskeye Gauss bulanıklığı uygula
        mask = cv2.GaussianBlur(mask, (5, 5), 100)
        
        # Konturları bul
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # En büyük konturu seç (muhtemelen el)
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        
        # Konturu yaklaştır (approximation)
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        # Konveks dışbükey gövdeyi bul
        hull = cv2.convexHull(cnt)
        
        # Alanları hesapla
        areaHull = cv2.contourArea(hull)
        areaCnt = cv2.contourArea(cnt)
        
        # Alan farkına göre oran hesapla
        areaRatio = ((areaHull - areaCnt) / areaCnt) * 100
        
        # Konveks boşlukları (defects) bul
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)
        
        l = 0  # Parmak sayacı
        
        # Her bir boşluk için analiz yap
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            
            # Üçgenin kenar uzunluklarını ve açısını hesapla
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            s = (a + b + c) / 2
            ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
            
            d = (2 * ar) / a
            
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57  # Dereceye çevir
            
            # Uygun açı ve mesafe şartları sağlanıyorsa bir parmak say
            if angle <= 90 and d > 30:
                l += 1
                cv2.circle(roi, far, 3, [255, 0, 0], -1)  # Boşluğa mavi daire çiz
            
            cv2.line(roi, start, end, [0, 255, 0], 2)  # Parmak çizgilerini çiz
        
        l += 1  # Son parmak
        
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Parmak sayısına göre ekrana yazı yazdır
        if l == 1:
            if areaCnt < 2000:
                cv2.putText(frame, 'Put your hand in the box', (0, 50), font, 1, (0, 0, 255), 3, cv2.LINE_AA)
            else:
                if areaRatio < 12:
                    cv2.putText(frame, '0', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                elif areaRatio < 17.5:
                    cv2.putText(frame, 'Best luck', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                else:
                    cv2.putText(frame, '1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        elif l == 2:
            cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        elif l == 3:
            if areaRatio < 27:
                cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame, 'ok', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        elif l == 4:
            cv2.putText(frame, '4', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        elif l == 5:
            cv2.putText(frame, '5', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        elif l == 6:
            cv2.putText(frame, 'reposition', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'reposition', (10, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
        
        # Maskeyi ve ana görüntüyü göster
        cv2.imshow('mask', mask)
        cv2.imshow('frame', frame)
    
    except:
        # Herhangi bir hata durumunda işlemi atla
        pass

    # ESC tuşuna basılırsa döngüyü kır
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
vid.release()
