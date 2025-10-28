import imutils
import cv2

image=cv2.imread("filim_foto.png") #resmi okuduk
image2=cv2.imread("renkli_sekiller.png")

(h,w,d)=image.shape #yükseklik genişlik ve derinlik
print("width= {}, height= {}, depth= {}".format(w,h,d))

(B,G,R)=image[100,50] #yükseklik,genişlik x=50,y=100
print("R={}, G={}, B={}".format(R,G,B))
# resim kırpma
ROI=image[90:170,500:580]

#resmi yeniden boyutlandıralım,
yeni=cv2.resize(image,(315,150))

#en boy oranına göre yeniden boyutlandırma
#burda w=300 olarak belirlenmiştir yani w=300 iken h'ı bulucaz ve yeni boyutumuzu oluşturucaz
r=300/w
dim=(300,int(h*r))
yeni_B=cv2.resize(image,dim)

#yeniden boyutlandırmanın kısa yolu
#imutils
yeni_boyut=imutils.resize(image,width=300)

#görüntüyü döndürme BİLGİ OpenCV görüntüyü döndürdükten sonra kırpılıp kırpılmadığıyla ilgilenmez
#bu nedenle yardımcı olarak imutiles kullanılır
rotated=imutils.rotate_bound(image,45) #45 derece döndür demek

#görüntüyü yumuşatma(bulanıklaştırma)

#sık kullanılan GaussianBlur
blurred=cv2.GaussianBlur(image,(11,11),0) # 11*11 çekirdekli bir bulanıklık sağlar
                                          # burdaki 0 is 11 e göre sigma değerinin otomatik hesaplanmasını sağlar

#görüntü üzerine çizim yapma(kare)
output=image.copy()
cv2.rectangle(output,(315,20),(445,165),(255,0,0),4)

#görüntü üzerine çizim yapma(daire)
output2=image.copy()
cv2.circle(output2,(340,95),25,(0,255,0),3)

#görüntü üzerine çizim yapma(çizgi)
output3=image.copy()
cv2.line(output3,(315,20),(445,165),(0,0,255),2)

#resim üzerine metin yazma
out=image.copy()
cv2.putText(out,"i am learning OpenCV",(15,15),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)

#NESNE SAYMA
gray=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
kenar=cv2.Canny(gray,20,150) #kenarları buldurur  20-150 kenar aralığı
_,thresh=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)
kontor=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
kontor=imutils.grab_contours(kontor)

for c in kontor:
    cv2.drawContours(image2,[c],-1,(240,0,159),3)

cv2.putText(image2,f"{len(kontor)} tane sekil var",(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(240,0,159),3) # -1 kodda hepsini yap anlamı taşır

# cv2.imshow("sayma",image2)

#EROZYONLAR ve GENİŞLEMELER
#threshold uyguladığımız şeklimizi erozyona uğratıp küçültelim
mask=thresh.copy()
mask=cv2.erode(mask,None,iterations=5) #iterations sayısı inceliği belirler
# cv2.imshow("erozyon",mask)

#genişleme uygulayalım
maske=thresh.copy()
maske=cv2.dilate(maske,None,iterations=5)
# cv2.imshow("geniş",maske)

#şimdi asıl resmimize maskemizi uygulayalım 
output5=cv2.bitwise_and(image2,image2,mask=mask)
cv2.imshow("maskelenmis",output5)




#metin için
# cv2.imshow("metin",out)

#çizimli görüntü(çizgi)
# cv2.imshow("cizgi",output3)

#çizimli görüntü(daire)
# cv2.imshow("daire",output2)

#çizimli görüntü(kare)
# cv2.imshow("cizim",output)

#bulanık görüntü
# cv2.imshow("blur",blurred)

#dönmüş görüntü
# cv2.imshow("rota",rotated)

#kısa boyutlandırma için
# cv2.imshow("yeni_boyut",yeni_boyut)

#orantılı boyut için
# cv2.imshow("O_boyut",yeni_B)

#yeni boyut için
# cv2.imshow("yeni boyut",yeni)

#ROI için
# cv2.imshow("ROI",ROI)

# cv2.imshow("Image",image)
cv2.waitKey(0)

