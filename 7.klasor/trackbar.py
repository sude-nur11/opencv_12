import cv2
import numpy as np

def bos():     # trackbarın çalışma şeklinden dolyı boş bir fonksiyon oluşturduk
    pass

canvas=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("canvas") # trackbarın nerede oluşturulacağını bildirmek için isim verdik

cv2.createTrackbar("R","canvas",0,255,bos)  # kırmızı trackbar için
cv2.createTrackbar("G","canvas",0,255,bos)
cv2.createTrackbar("B","canvas",0,255,bos)
switch="0:OFF ,1:ON"
cv2.createTrackbar("switch","canvas",0,1,bos)

while True:

    r=cv2.imshow("canvas",canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r=cv2.getTrackbarPos("R","canvas")
    g=cv2.getTrackbarPos("G","canvas")
    b=cv2.getTrackbarPos("B","canvas")
    s=cv2.getTrackbarPos("switch","canvas")
    
    if s==0:
        canvas[:]=(0,0,0)  #canvas[:] oluşturduğumuz penceredeki bütün pikselleri kasteder yani tüm pencereyi
    if s==1:
        canvas[:]=[b,g,r]  #oluşturduğumuz trackbarların pozisyonlarını anlık olarak pencereye bu kısımda aktarmış olduk

cv2.destroyAllWiondows()

