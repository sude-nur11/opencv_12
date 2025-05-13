import cv2

img=cv2.imread("2.1 contour1.png.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th1=cv2.threshold(gray,150,200,cv2.THRESH_BINARY)

contours,_=cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE degerleri varsayılan olarak yazılır hata almamak için kullanılır

cv2.drawContours(img,contours,-1,(255,0,0),5) # -1 yerine 0 yazarsakta sadece resmin bulundugu çerçeveyi çizer

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()