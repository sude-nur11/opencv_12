import cv2
import numpy as np

def image_stats(image):
    # Her kanalın ortalama ve standart sapmasını hesapla
    (l, a, b) = cv2.split(image)
    return (l.mean(), l.std(), a.mean(), a.std(), b.mean(), b.std())

def color_transfer(source, target):
    # BGR → L*a*b* (float32)
    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
    target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

    # Kanal istatistikleri
    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

    # Hedef kanallarını ayır ve ortalamayı çıkar
    (l, a, b) = cv2.split(target)
    l -= lMeanTar; a -= aMeanTar; b -= bMeanTar

    # Std oranıyla ölçekle, kaynak ortalamasını ekle
    l = (lStdTar / lStdSrc) * l + lMeanSrc
    a = (aStdTar / aStdSrc) * a + aMeanSrc
    b = (bStdTar / bStdSrc) * b + bMeanSrc

    # Değerleri [0,255] aralığında tut
    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    # L*a*b* → BGR dönüşümü
    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
    return transfer



# Örnek kullanım
if __name__ == "__main__":
    source = cv2.imread("sonbahar.jpg")
    target = cv2.imread("agaclar.jpg")
    transfer = color_transfer(source, target)

    

    cv2.imshow("Kaynak", source)
    cv2.imshow("Hedef", target)
    cv2.imshow("Aktarım", transfer)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
