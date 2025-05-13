import cv2

img=cv2.imread("dunya-haritasi-2.jpg")
cv2.namedWindow("harita-bgr",cv2.WINDOW_NORMAL)
cv2.namedWindow("harita-rgb",cv2.WINDOW_NORMAL)
cv2.namedWindow("harita-hsv",cv2.WINDOW_NORMAL)
cv2.namedWindow("harita-gray",cv2.WINDOW_NORMAL)
#bgr dan rgb ye dönüştürme
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#bgr dan hsv ye dönüştürme
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#bgr dan gray e dönüştürme
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("harita-bgr",img)
cv2.imshow("harita-rgb",img_rgb)
cv2.imshow("harita-hsv",img_hsv)
cv2.imshow("harita-gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()