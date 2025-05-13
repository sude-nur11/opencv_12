import cv2
import numpy as np

img=cv2.imread("5.1 coins.jpg.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray,5)


circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=15,maxRadius=89)
# burdaki 4 sayisiyla oynayarak goruntudeki daireleri cevreleyebildik
'''
1: Girdi görüntüsü ile Hough uzayı arasındaki çözünürlük oranı.

img.shape[0]/4: Tespit edilen dairelerin merkezleri arasındaki minimum mesafe.

param1=200: Canny kenar dedektörü için üst eşik değeri.

param2=10: Daire tespiti için eşik değeri. Düşük değerler daha fazla daire tespit eder, ancak yanlış pozitifler artabilir.

minRadius=15: Tespit edilecek dairelerin minimum yarıçapı.

maxRadius=89: Tespit edilecek dairelerin maksimum yarıçapı'''

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img, (i[0],i[1]), i[2], (0,255,0),2)

# np.around(circles) kayan noktalı sayıları tam sayıya yuvarlar
# np.uint16 yuvarlanmış sayıları tam sayı formatına donuşturur
# (i[0],i[1]) dairenin x ve y kordinatlarını temsil eder
# i[2] dairenin yarı çapını temsil eder     

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()