import cv2

vid = cv2.VideoCapture("15.1 eye_motion.mp4.mp4")

while 1:
    
    ret, frame = vid.read()
    if ret is False: 
        break

    # İlgi alanını (ROI) belirle: [y1:y2, x1:x2] (göz bölgesi)
    roi = frame[80:210, 230:450]
    rows, cols, _ = roi.shape  # ROI'nin boyutlarını al

    # ROI'yi gri tonlamalı hale çevir (göz bebeği tespiti için)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Eşikleme (thresholding) uygula: 
    # Koyu pikselleri (göz bebeği) beyaz, diğerlerini siyah yap
    _, threshold = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY_INV)

    # Konturları bul (göz bebeği sınırlarını tespit et)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Konturları alanlarına göre büyükten küçüğe sırala
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    # En büyük kontur için işlem yap (göz bebeği olduğunu varsay)
    for cnt in contours:
        # Konturun sınırlayıcı dikdörtgenini al
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        # ROI üzerine göz bebeği dikdörtgenini çiz (mavi)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Göz bebeğinin merkezinden dikey/yatay çizgiler çiz (yeşil)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        break  # Sadece en büyük konturla işlem yap ve döngüden çık
    
    # İşlenmiş ROI'yi ana frame'e geri yerleştir
    frame[80:210, 230:450] = roi
    
    cv2.imshow("frame", frame)
  
    if cv2.waitKey(80) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()