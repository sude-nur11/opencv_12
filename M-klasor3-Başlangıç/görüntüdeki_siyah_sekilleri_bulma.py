import cv2      
import numpy as np  
import imutils   

image = cv2.imread("siyah_sekiller.png")

#Görüntü ojunmuyorsa hata ver
if image is None:
    raise FileNotFoundError("Görüntü bulunamadı. Dosya adını ve konumunu kontrol et!")

#Siyah renk aralığını belirle (BGR formatında)
#alt: saf siyah, üst: çok koyu gri
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])

#Bu aralıkta kalan pikselleri maske olarak al
#Siyah olan yerler beyaz hale gelir (maskede)
mask = cv2.inRange(image, lower, upper)

#Maskedeki konturları (şekil sınırlarını) bul
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  # OpenCV sürüm farklarını çözer

#Kaç şekil bulunduğunu yaz
print(f"{len(cnts)} siyah şekil bulundu.")

#Her konturu sırayla çiz
for c in cnts:
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)  # Yeşil kenarlık
    cv2.imshow("Sonuç", image)
    cv2.waitKey(500)  # Her şekli 0.5 sn göster

cv2.imshow("Tüm Şekiller", image)
cv2.imshow("Maske (Siyah alanlar beyaz)", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
