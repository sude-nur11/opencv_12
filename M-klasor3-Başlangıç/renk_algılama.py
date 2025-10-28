import cv2
import numpy as np

image = cv2.imread("pokemon_games.png")

# bu kısımda görüntü okunamamışsa uyarı verir ve çıkar
if image is None:
    print("Görüntü bulunamadı! Dosya adını veya yolu kontrol et.")
    exit()

# Tespit etmek istediğimiz renk aralıklarını (BGR formatında) tanımla
# Her bir aralık: [Alt sınır], [Üst sınır]
# Bu değerler kırmızı, mavi, sarı ve gri tonlarını temsil eder.
boundaries = [
    ([17, 15, 100], [50, 56, 200]),   # Kırmızı aralığı
    ([86, 31, 4], [220, 88, 50]),     # Mavi aralığı
    ([25, 146, 190], [62, 174, 250]), # Sarı aralığı
    ([103, 86, 65], [145, 133, 128])  # Gri aralığı
]

#Her renk aralığı için işlemleri yap
for (lower, upper) in boundaries:
    # Alt ve üst sınırları NumPy dizisine çevir (OpenCV bunu ister)
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    #Belirtilen renk aralığında kalan pikselleri tespit et
    # Beyaz (255) → o renk aralığında, Siyah (0) → dışında
    mask = cv2.inRange(image, lower, upper)

    #Maskeyi kullanarak orijinal görüntüden sadece o renk bölgesini al
    output = cv2.bitwise_and(image, image, mask=mask)

    #Görüntüleri yan yana göster (solda orijinal, sağda sadece tespit edilen renk)
    cv2.imshow("Color Detection", np.hstack([image, output]))

    cv2.waitKey(0)

cv2.destroyAllWindows()
