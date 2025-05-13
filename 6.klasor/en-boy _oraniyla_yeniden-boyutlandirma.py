import cv2

def boyutlandirma(img,en=None,boy=None,inter=cv2.INTER_AREA):# inter=cv2.INTER_AREA boyutlandirma fonksiyonlarinin yapisinde vardir yazilmalidir

    dimension=None
    (b,e)= img.shape[:2] # burdaki [:2] iki boyutlu resimdeki en ve boyu buldurur
    
    if en ==None and boy==None:
        return img
    if en==None:
        r=boy/float(b)
        dimension= (int(e*r),boy)
    else:
        r=en/float(e)
        dimension=(en,int(b*r))
    return cv2.resize(img,dimension,interpolation=inter)
img=cv2.imread("dunya-haritasi-2")
img1=boyutlandirma(img,en=None,boy=600,inter=cv2.INTER_AREA) # yeni boyut

cv2.imshow("orijinal",img)
cv2.imshow("resized",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()



