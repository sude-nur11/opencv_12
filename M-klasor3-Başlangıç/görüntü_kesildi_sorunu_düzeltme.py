import cv2
import numpy as np
import imutils
import argparse

# Argüman okuma kısmı (şimdilik yorum satırında)
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#     help="path to the image file")
# args = vars(ap.parse_args())

image = cv2.imread("hap_01.png")

#Görüntüyü gri tonlamaya çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Gürültüyü azaltmak için bulanıklaştır
gray = cv2.GaussianBlur(gray, (3, 3), 0)

#Kenarları tespit et (Canny algoritması)
edged = cv2.Canny(gray, 20, 100)

#Konturları (nesne sınırlarını) bul
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

if len(cnts) > 0:
    #En büyük konturu (alan olarak) al
    c = max(cnts, key=cv2.contourArea)

    #Aynı boyutta boş bir maske
    mask = np.zeros(gray.shape, dtype="uint8")

    #En büyük konturu maskeye çiz
    cv2.drawContours(mask, [c], -1, 255, -1)

    #bu bölgede konturları sınırlayıcı dikdörtgenine alıyoruz
    (x, y, w, h) = cv2.boundingRect(c)

    #ROI (Region of Interest – ilgi alanı) çıkar
    imageROI = image[y:y + h, x:x + w]
    maskROI = mask[y:y + h, x:x + w]

    #Maskeyi uygulayarak yalnızca kontur alanını alıyoruz
    imageROI = cv2.bitwise_and(imageROI, imageROI, mask=maskROI)

    #1. Döngü: rotate() — bu yöntem görüntüyü kesebilir (problemli döndürme)
    for angle in np.arange(0, 360, 15):
        rotated = imutils.rotate(imageROI, angle)
        cv2.imshow("Rotated (Problematic)", rotated)
        cv2.waitKey(0)

    #2. Döngü: rotate_bound() — bu yöntem görüntünün kesilmesini önler
    for angle in np.arange(0, 360, 15):
        rotated = imutils.rotate_bound(imageROI, angle)
        cv2.imshow("Rotated (Correct)", rotated)
        cv2.waitKey(0)

