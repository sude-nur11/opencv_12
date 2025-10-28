import argparse
import imutils
import cv2
# Argüman ayrıştırıcısını oluşturun ve argümanları ayrıştırın
ap=argparse.ArgumentParser()
ap.add_argument("-i","--input",required=True,help="path to input image")
ap.add_argument("-o","--output",required=True,help="path to output image")
args=vars(ap.parse_args())

# Giriş görüntüsünü diskten yükleyin
image=cv2.imread(args["input"])
# Görüntüyü gri tonlamaya dönüştürün, bulanıklaştırın ve eşikleyin
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
_,thresh=cv2.threshold(blurred,60,255,cv2.THRESH_BINARY_INV)
# görüntüden konturları çıkarın
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# konturların üzerinden geçin ve bunları giriş görüntüsünün üzerine çizin
for c in cnts:
	cv2.drawContours(image, [c], -1, (0, 255,0), 2)
# Görüntüdeki toplam şekil sayısını görüntüleyin
text = "I found {} total shapes".format(len(cnts))
cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255,0), 2)    
# çıktı görüntüsünü diske yaz
cv2.imwrite(args["output"], image)

#python python_ile_komut_satırı_argümanlarını_ayrıştırma.py -i input.png -o output.png      (bunu kullandık terminalde)