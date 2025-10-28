import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local
from pyimagesearch.transform import four_point_transform

image = cv2.imread("gercek_bilet.jpg")  

if image is None:
    raise Exception("Görüntü yüklenemedi")

ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height=500)

# Gri tonlama, bulanıklaştırma, kenar bulma
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

# Konturları bul ve en büyük dörtgeni seç
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

screenCnt = None
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    raise Exception("Belge bulunamadı!")

# Perspektif dönüşümü (belgeyi düzleştir)
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

# Griye çevir ve adaptif eşik uygula
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset=10, method="gaussian")
warped = (warped > T).astype("uint8") * 255

cv2.imshow("Edged", edged)
cv2.imshow("Orijinal", imutils.resize(orig, height=650))
cv2.imshow("Taranmış Belge", imutils.resize(warped, height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()
