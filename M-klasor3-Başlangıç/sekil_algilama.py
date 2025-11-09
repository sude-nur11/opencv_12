import cv2
import imutils
from shapedetector import ShapeDetector

image = cv2.imread("farkli_sekiller.png")

# Görüntüyü küçült (işlem daha hızlı ve sabit olur)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# Gri tonlamaya çevir > Gürültüyü azaltmak için bulanıklaştır > İkili (siyah-beyaz) hale getir
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# Konturları bul (nesne sınırları)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Şekil dedektörünü başlat
sd = ShapeDetector()

# Her konturu sırayla işle
for c in cnts:
    # Konturun merkezini hesapla
    M = cv2.moments(c)
    if M["m00"] == 0:  # Bölme hatasını önle
        continue
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)

    # Şekli tespit et
    shape = sd.detect(c)

    # Koordinatları orijinal boyuta ölçekle
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    # Konturu çiz ve şekil adını yaz
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX - 30, cY),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Şekil Algılama", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"ben sude gfeliyorummmmmm"
