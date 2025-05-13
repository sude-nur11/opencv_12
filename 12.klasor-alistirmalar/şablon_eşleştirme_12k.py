import cv2
import numpy as np

image_path = "4.2 starwars.jpg.jpg"
template_path = "5.2 starwars2.jpg.jpg"

# Ana görüntüyü yükle ve gri tonlamaya çevir
img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Şablon görüntüsünü gri tonlamada yükle
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]  # Şablonun genişlik ve yüksekliğini al

# Şablon eşleştirme yap
result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# Korelasyon değeri %95'ten büyük olan yerleri bul
location = np.where(result >= 0.95)

# Eşleşen bölgelerin etrafına dikdörtgen çiz
for point in zip(*location[::-1]):
    cv2.rectangle(img, point, (point[0]+w, point[1]+h), (0,255,0), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()