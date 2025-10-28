from pyimagesearch.sekil_tespit import SekilTespit
from pyimagesearch.renk_tespit import RenkTespit
# import argparse
import imutils
import cv2

# Komut satırından resim yolu alma
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Giris resim yolu")
# args = vars(ap.parse_args())
# image = cv2.imread(args["image"])

# Görüntüyü yükle ve yeniden boyutlandır

image = cv2.imread("renk_algi_sekiller.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# Hafif bulanıklaştır, gri ve LAB renk uzayına çevir
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

# Görüntüyü eşikle (şekilleri ayır)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

# Konturları bul
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Sınıfları başlat
sd = SekilTespit()
cl = RenkTespit()

# Her konturu işle
for c in cnts:
    # Merkez noktayı bul
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)

    # Şekli ve rengi tespit et
    shape = sd.detect(c)
    color = cl.label(lab, c)

    # Konturu orijinal boyuta göre ölçekle
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")

    # Ekrana çiz ve etiket ekle
    text = f"{color} {shape}"
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

cv2.imshow("Sonuc", image)
cv2.waitKey(0)

