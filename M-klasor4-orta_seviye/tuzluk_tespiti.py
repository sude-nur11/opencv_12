import cv2
import numpy as np

# görüntüyü yükle
image = cv2.imread("yat.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Laplacian veya Sobel filtreyle kenar yoğunluğu (enerji) bul
lap = cv2.Laplacian(gray, cv2.CV_64F)
saliencyMap = np.absolute(lap)
saliencyMap = cv2.GaussianBlur(saliencyMap, (9,9), 0)

# normalize et
saliencyMap = cv2.normalize(saliencyMap, None, 0, 255, cv2.NORM_MINMAX).astype("uint8")

# sonuçları göster
cv2.imshow("Orijinal", image)
cv2.imshow("Belirginlik Haritası (Laplacian)", saliencyMap)
cv2.waitKey(0)
cv2.destroyAllWindows()
