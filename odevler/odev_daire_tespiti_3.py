import cv2
import numpy as np

# Görüntüyü oku ve yeniden boyutlandır
img = cv2.imread("bozuk_paralar_3.jpg")  # Dosya adını yüklediğin görsele göre güncelle
img = cv2.resize(img, (512, 512))
output = img.copy()

# Griye çevir ve bulanıklaştır
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 11)

# Daireleri Hough Circle yöntemi ile bul
circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=100,
    param2=30,
    minRadius=30,
    maxRadius=90
)

# Daire varsa çiz
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]
        cv2.circle(output, center, radius, (0, 0, 255), 3)

    # Daire sayısını yazdır
    cv2.putText(output, f"{len(circles[0])} tane daire var", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Sonuçları göster
cv2.imshow("Tespit Edilen Paralar (Dairelerle)", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
