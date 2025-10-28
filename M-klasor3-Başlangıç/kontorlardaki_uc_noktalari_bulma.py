import cv2
import imutils

image = cv2.imread("el.png")

# Gri tonlamaya çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# bulanıklaştır
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# İkili görüntü oluştur
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]

# Küçük gürültüleri temizle
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# Konturları bul
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# En büyük konturu seç (genellikle asıl nesne olur)
c = max(cnts, key=cv2.contourArea)

# Kontur üzerindeki uç noktaları bul
extLeft = tuple(c[c[:, :, 0].argmin()][0])   # En sol nokta
extRight = tuple(c[c[:, :, 0].argmax()][0])  # En sağ nokta
extTop = tuple(c[c[:, :, 1].argmin()][0])    # En üst nokta
extBot = tuple(c[c[:, :, 1].argmax()][0])    # En alt nokta

# Konturu ve uç noktaları çiz
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)      # Sarı kontur
cv2.circle(image, extLeft, 8, (0, 0, 255), -1)          # Sol: Kırmızı
cv2.circle(image, extRight, 8, (0, 255, 0), -1)         # Sağ: Yeşil
cv2.circle(image, extTop, 8, (255, 0, 0), -1)           # Üst: Mavi
cv2.circle(image, extBot, 8, (255, 255, 0), -1)         # Alt: Camgöbeği

# Sonucu göster
cv2.imshow("Uç Noktalar", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
