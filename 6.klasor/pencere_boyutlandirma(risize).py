import cv2

img=cv2.namedWindow("canvas")
img=cv2.imread("dunya-haritasi-2.jpg")

cv2.resize(img,(20,20))   # istedigimiz degerleri vererek resmi yeniden  boyutlandirmamizi saglar

cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()