import cv2
import numpy as np
import imutils
# import argparse

# Komut satırından argüman almak için ayar
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Görüntü dosyasının yolu")
# args = vars(ap.parse_args())
# image = cv2.imread(args["image"])


image = cv2.imread("barkod.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Scharr gradyan büyüklük temsili oluştur
ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

# Y-gradyanını X-gradyanından çıkar
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

# Görüntüyü bulanıklaştır ve eşikle
blurred = cv2.blur(gradient, (9, 9))
_, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

# Morfolojik kapanış işlemi (boşlukları kapatmak için)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Gürültüyü azaltmak için erozyon ve genişleme uygula
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)

# Konturları bul ve en büyük olanı seç
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# En büyük konturun döndürülmüş sınırlayıcı kutusunu hesapla
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
box = np.int0(box)

# Algılanan barkodun etrafına yeşil kutu çiz
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

cv2.imshow("Detected Barcode", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
