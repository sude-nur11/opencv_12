import cv2
import numpy as np

path1 = "1.1 aircraft.jpg.jpg"
path2 = "1.1 aircraft-2.jpg.jpg"

# Görüntüleri oku ve yeniden boyutlandır
img1 = cv2.imread(path1)
img1 = cv2.resize(img1, (640, 550))
img2 = cv2.imread(path2)
img2 = cv2.resize(img2, (640, 550))

# Gürültü azaltma için median blur uygula
img3 = cv2.medianBlur(img1, 7)

# İki görüntü arasındaki farkı hesapla
diff = cv2.subtract(img1, img3)
b, g, r = cv2.split(diff)

# Tamamen aynı olup olmadığını kontrol et
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("Tamamen aynı")
else:
    print("Tamamen aynı değil")

# Fark görüntüsünü göster
cv2.imshow("Difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()