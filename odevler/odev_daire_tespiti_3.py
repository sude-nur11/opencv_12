import cv2
import numpy as np


img = cv2.imread("bozuk_paralar_3.jpg") 
img = cv2.resize(img, (512, 512))
output = img.copy()

# Griye çevir ve bulanıklaştır
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 11)

# --- WATERSHED ALGORİTMASI ---

# Binary threshold (ters)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Gürültü temizleme
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Arka plan
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Ön plan
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# Bilinmeyen alan
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker etiketleme
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Watershed uygula 
_ = cv2.watershed(img.copy(), markers)

# --- HOUGH CIRCLES ALGORİTMASI ---

circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=100,
    param2=30,
    minRadius=30,
    maxRadius=90
)

# Daireleri çiz
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]
        cv2.circle(output, center, radius, (0, 0, 255), 3)

    # Daire sayısını yaz
    cv2.putText(output, f"{len(circles[0])} tane daire var", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)


cv2.imshow("Tespit Edilen Paralar (Dairelerle)", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
