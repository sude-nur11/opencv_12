import cv2
import numpy as np
import imutils

# Konturları belirtilen yöne göre sıralayan fonksiyon
def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method in ["right-to-left", "bottom-to-top"]:
        reverse = True
    if method in ["top-to-bottom", "bottom-to-top"]:
        i = 1

    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    cnts, boundingBoxes = zip(*sorted(zip(cnts, boundingBoxes),
                                      key=lambda b: b[1][i], reverse=reverse))
    return cnts, boundingBoxes

# Konturları numaralandırarak çizer
def draw_contour(image, c, i):
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(image, f"#{i + 1}", (cX - 20, cY),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    return image


image = cv2.imread("logolar.png")
accumEdged = np.zeros(image.shape[:2], dtype="uint8")

# Renk kanallarında kenarları birleştir
for chan in cv2.split(image):
    chan = cv2.medianBlur(chan, 11)
    edged = cv2.Canny(chan, 50, 200)
    accumEdged = cv2.bitwise_or(accumEdged, edged)

cv2.imshow("Edges", accumEdged)

# Konturları bul ve en büyük 4 tanesini al
cnts = cv2.findContours(accumEdged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:4]

# Sıralama öncesi konturları çiz
orig = image.copy()
for (i, c) in enumerate(cnts):
    orig = draw_contour(orig, c, i)
cv2.imshow("Unsorted", orig)

# Konturları sıralayıp çiz
(cnts, _) = sort_contours(cnts, method="top-to-bottom")
for (i, c) in enumerate(cnts):
    draw_contour(image, c, i)

cv2.imshow("Sorted", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
