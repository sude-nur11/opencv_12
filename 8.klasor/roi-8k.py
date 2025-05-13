#roi ===> resimdeki ilgi alanı
import cv2


img=cv2.imread("dunya-haritasi-2.jpg")
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
print(img.shape[:2]) #çıktı = (2576, 3864)

roi=img[1140:1230,2080:2276] # TÜRKİYE UUUUUUU

#yukarıkadi kısımda once ye ekseninde sonrada x ekseninde tarama yaptık

cv2.imshow("roiii",roi)
cv2.imshow("image",img)
cv2.waitKey(0)  
cv2.destroyAllWindows()