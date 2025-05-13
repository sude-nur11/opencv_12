import cv2

img = cv2.imread("4.2 starwars.jpg.jpg")

# Görüntüye bulanıklık ekle (9x9 median filtre)
blurry_img = cv2.medianBlur(img, 9)

# Laplacian varyansı ile netlik ölçümü 
laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()
print("Laplacian Varyans Değeri:", laplacian)

# Netlik kontrolü (500 eşik değeri)
if laplacian < 500:
    print("Bulanik Goruntu")
else:
    print("Net Goruntu")

# Orijinal ve bulanık görüntüyü göster
cv2.imshow("Orijinal Görüntü", img)
cv2.imshow("Bulanık Görüntü", blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()