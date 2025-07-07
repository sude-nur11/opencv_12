import cv2

# Görüntüyü ve cascade dosyalarını yükle
img = cv2.imread('4.1 smile.jpg.jpg')
smile_cascade = cv2.CascadeClassifier('4.2 smile.xml.xml')
face_cascade = cv2.CascadeClassifier('4.1 frontalface.xml.xml')

# Yüz tespiti için gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    # Yüzü kırmızı dikdörtgenle işaretle
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    # Yüz bölgesini (ROI) al
    roi_gray = gray[y:y+h, x:x+w]  # Düzeltme: y,x sırası önemli!
    roi_img = img[y:y+h, x:x+w]
    
    # Gülümseme tespiti yap
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.3, 5)
    for (ex, ey, ew, eh) in smiles:
        # Gülümsemeyi yeşil dikdörtgenle işaretle
        cv2.rectangle(roi_img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

# Sonucu göster
cv2.imshow('Yüz ve Gülümseme Tespiti', img)
cv2.waitKey(0)
cv2.destroyAllWindows()