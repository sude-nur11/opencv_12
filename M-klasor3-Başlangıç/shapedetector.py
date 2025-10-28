import cv2

class ShapeDetector:
    def __init__(self):
        pass  # Şimdilik başlangıçta bir işlem yapılmıyor

    def detect(self, c):
        # Başlangıçta şekil adı bilinmiyor
        shape = "tanımlanamayan"

        # Konturun çevresini (perimetre) hesapla
        peri = cv2.arcLength(c, True)

        # Konturu sadeleştir (az nokta ile benzer form)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # 3 köşe → Üçgen
        if len(approx) == 3:
            shape = "ucgen"

        # 4 köşe → Kare veya Dikdörtgen
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "kare" if 0.95 <= ar <= 1.05 else "dikdortgen"

        # 5 köşe → Beşgen
        elif len(approx) == 5:
            shape = "besgen"

        # Daha fazlası → Daire
        else:
            shape = "daire"

        return shape
