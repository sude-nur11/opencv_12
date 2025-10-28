import numpy as np
import argparse
import imutils
import cv2

# Argümanı oluşturun Argümanları ayrıştırın ve ayrıştırın

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the image file")
# args = vars(ap.parse_args())


image=cv2.imread("teknofest.jpg")
#dönme açıları üzerinde döngü

'''for range in np.arange(0,360,15):  #(0,360,15)==> 0 dan 360 a kadar her seferrinde 15 derece döndür demek 
    rotated=imutils.rotate(image,range)
    cv2.imshow("dön",rotated)
    cv2.waitKey(0)'''

#döndü açıları üzerinde döngü ama bu sefer resimde bir kesilme işlemi olmuycak
# yani bir dütün olarak döndüğünü gözlemliycez

'''for range1 in np.arange(0,360,15):
    rota=imutils.rotate_bound(image,range1)
    cv2.imshow("dön1",rota)
    cv2.waitKey(0)'''

def rotate_bound(image,angle):  # görüntü ve açı parametrelerini alıyor
    (h,w)=image.shape[:2]  # [:2] bu ifade alıma 3 değerden sadece 2 tanesini almamızı sağlar yani yükseklik ve genişliği 
    (cX,cY)=(w//2,h//2) # merkez kordinatlar
    M=cv2.getRotationMatrix2D((cX,cY), -angle,1.0)
    # sin ve cos değerleri
    cos=np.abs(M[0,0])
    sin=np.abs(M[0,1])
    
	# Görüntünün yeni sınırlayıcı boyutlarını hesaplayın
    nW=int((h*sin)+(w*cos))
    nH=int((h*cos)+(w*sin))
    
	# Çeviriyi hesaba katmak için döndürme matrisini ayarlayın
    M[0,2]+=(nW/2)-cX
    M[1,2]+=(nH/2)-cY

    # Gerçek dönüşü gerçekleştirin ve görüntüyü döndürün
    return cv2.warpAffine(image,M,(nW,nH))
