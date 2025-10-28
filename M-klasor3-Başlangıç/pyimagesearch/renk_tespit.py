from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

class RenkTespit:
    def __init__(self):
        colors = OrderedDict({
            "kirmizi": (255, 0, 0),
            "yesil": (0, 255, 0),
            "mavi": (0, 0, 255)
        })

        # Renkleri tutacak LAB dizisi ve isim listesi
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []

        # Her bir rengi LAB formatına çevir
        for (i, (name, rgb)) in enumerate(colors.items()):
            self.lab[i] = rgb
            self.colorNames.append(name)

        # RGB renk uzayını LAB’a dönüştür
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

    def label(self, image, c):
        # Kontur (şekil) için maske oluştur
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        
        # Gürültüyü azaltmak için maskeyi biraz aşındır
        mask = cv2.erode(mask, None, iterations=2)

        # Maskelenen bölgenin ortalama LAB değerini al
        mean = cv2.mean(image, mask=mask)[:3]

        # En yakın rengi bulmak için başlangıç değeri
        minDist = (np.inf, None)

        # Bilinen renklerle karşılaştır
        for (i, row) in enumerate(self.lab):
            d = dist.euclidean(row[0], mean)
            if d < minDist[0]:
                minDist = (d, i)

        # En yakın renk adını döndür
        return self.colorNames[minDist[1]]
