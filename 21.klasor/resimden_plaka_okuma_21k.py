import cv2                  
import numpy as np           
import pytesseract           
import imutils              

img = cv2.imread("9.1 licence_plate.jpg.jpg")

# Görüntüyü gri tona çevir (renk bilgisi olmadan işlem daha kolay)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültüyü azaltmak için bilateral filtre uygula
filtered = cv2.bilateralFilter(gray, 6, 250, 250)

# Kenarları tespit et (Canny algoritması)
edged = cv2.Canny(filtered, 30, 200)

# Kenarları (contour) bul
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)  # Contour'ları uygun formatta al

# Contour'ları alana göre sırala ve en büyük 10 tanesini al
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

screen = None  # Plaka olabilecek alanı tutacak değişken

# Her bir konturu tek tek incele
for c in cnts:
    epsilon = 0.018 * cv2.arcLength(c, True)  # Konturun çevresinin yaklaşık %1.8’i
    approx = cv2.approxPolyDP(c, epsilon, True)  # Kontura yaklaşık dörtgen çizer

    # Eğer kontur dört kenarlıysa, bu plaka olabilir
    if len(approx) == 4:
        screen = approx
        break

# Maske oluştur ve sadece plakanın olduğu kısmı seç
mask = np.zeros(gray.shape, np.uint8)  # Boş bir siyah maske
new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)  # Plakayı maskeye çiz
new_img = cv2.bitwise_and(img, img, mask=mask)  # Görüntü ile maskeyi birleştir

# Plakanın koordinatlarını bul
(x, y) = np.where(mask == 255)  # Maskedeki beyaz bölgelerin koordinatları
(topx, topy) = (np.min(x), np.min(y))
(bottomsx, bottomsy) = (np.max(x), np.max(y))

# Gri görüntüden sadece plaka kısmını kırp
cropped = gray[topx:bottomsx+1, topy:bottomsy+1]

# Tesseract kullanarak görüntüden metni oku
text = pytesseract.image_to_string(cropped, lang="eng")
print("text=", text)  # Plaka üzerindeki yazıyı yazdır

cv2.waitKey(0)
cv2.destroyAllWindows()
