import cv2
import numpy as np
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import argparse

# Argüman al
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Cevap kağıdı resmi")
# args = vars(ap.parse_args())
# image = cv2.imread(args["image"])

# Cevap anahtarı
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}


# Resmi yükle ve ön işlem
image = cv2.imread("baloncuk_test.jpg")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

# Belge konturu bul
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None
if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            docCnt = approx
            break
if docCnt is None:
    raise Exception("Belge bulunamadı!")

# Perspektif düzeltme
paper = four_point_transform(orig, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))

# Binarizasyon
thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Soru konturlarını bul
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
    if w >= 20 and h >= 20 and 0.9 <= ar <= 1.1:
        questionCnts.append(c)

questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]

# Yanıtları oku ve puanla
correct = 0
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
    if q not in ANSWER_KEY:
        continue 
    cnts_row = contours.sort_contours(questionCnts[i:i + 5])[0]
    bubbled = None
    for (j, c) in enumerate(cnts_row):
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)
        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)

    k = ANSWER_KEY[q]
    color = (0, 0, 255)
    if k == bubbled[1]:
        color = (0, 255, 0)
        correct += 1
    cv2.drawContours(paper, [cnts_row[k]], -1, color, 3)

# Sonucu göster
score = (correct / len(ANSWER_KEY)) * 100
print(f"[INFO] score: {score:.2f}%")
cv2.putText(paper, f"{score:.2f}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", orig)
cv2.imshow("Graded Exam", paper)
cv2.waitKey(0)
cv2.destroyAllWindows()
