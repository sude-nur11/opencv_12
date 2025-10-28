# Gerekli paketleri içe aktar
import argparse  # Terminalden argüman almak için
import imutils   # OpenCV sürümlerinde uyumluluk için
import cv2       # OpenCV kütüphanesi

# Terminalden görüntü yolunu alacak argümanı ayarla
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="İşlenecek görüntünün yolu")
# args = vars(ap.parse_args())          👉#TERMİNAL YOLU: python kontor_merkezi.py --image farkli_sekiller.png
# Görüntüyü yükle
# image = cv2.imread(args["image"])


image = cv2.imread("farkli_sekiller.png")

# Görüntüyü gri tonlamaya çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# gürültüyü azaltmak için
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Görüntüyü ikili hale getir (threshold)
# Şekiller beyaz, arka plan siyah olacak
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# Konturları bul
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  # OpenCV sürümleri uyumu

# Her bir kontur üzerinde döngü
for c in cnts:
    # Konturun merkezini (centroid) hesapla
    M = cv2.moments(c)
    # Alanın sıfır olup olmadığını kontrol et (sıfır olursa bölme hatası olur)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    # Konturu çiz (yeşil renk, kalınlık 2)
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

    # Merkeze beyaz bir nokta çiz (radius 7)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)

    # Merkezin yanına "center" yaz
    cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Contours & Centers", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
