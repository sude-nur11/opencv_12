from panorama.stitcher import Stitcher
# import argparse
import imutils
import cv2

# Komut satırı argümanlarını al
# ap = argparse.ArgumentParser()
# ap.add_argument("-f", "--first", required=True, help="Birinci (sol) görüntü yolu")
# ap.add_argument("-s", "--second", required=True, help="İkinci (sağ) görüntü yolu")
# args = vars(ap.parse_args())
# imageA = cv2.imread(args["first"])
# imageB = cv2.imread(args["second"])

imageA = cv2.imread("panorama-1.jpg")
imageB = cv2.imread("panorama-2.jpg")

# Daha hızlı işlem için yeniden boyutlandır
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# Stitcher sınıfını oluştur ve panoramayı oluştur
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Panorama Result", result)
cv2.waitKey(0)
