import cv2

class SekilTespit:
    def __init__(self):
        pass

    def detect(self, c):
        # Kontur çevresini al
        peri = cv2.arcLength(c, True)
        # Konturu basitleştir
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        shape = "tanimsiz"

        # Köşe sayılarına göre şekli belirle
        if len(approx) == 3:
            shape = "ucgen"
        elif len(approx) == 4:
            # Kare mi dikdörtgen mi kontrolü
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "kare" if 0.95 <= ar <= 1.05 else "dikdortgen"
        elif len(approx) == 5:
            shape = "besgen"
        else:
            shape = "daire"

        return shape
