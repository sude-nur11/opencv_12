import cv2
# import numpy as np

img_harita=cv2.imread("dunya-haritasi-2.jpg")
img_duvar=cv2.imread("duvar_puruzu-1.jpg")


# cv2.namedWindow("blur",cv2.WINDOW_NORMAL)
# cv2.namedWindow("orijinal",cv2.WINDOW_NORMAL)
# cv2.namedWindow("median",cv2.WINDOW_NORMAL)
# cv2.namedWindow("median_O",cv2.WINDOW_NORMAL)
cv2.namedWindow("bilateral",cv2.WINDOW_NORMAL)
cv2.namedWindow("bilateral_O",cv2.WINDOW_NORMAL)


blur=cv2.blur(img_harita,(11,11)) # sayi ile ilgili kısma pozitif tek sayılar yazılır
median_B=cv2.medianBlur(img_duvar,121) # pürüzlü resimleri yumuşatır
bilateral=cv2.bilateralFilter(img_duvar,9,125,125) # pürüzlü resimleri yumuşatır

# cv2.imshow("blur",blur)
# cv2.imshow("orijinal",img_harita)
# cv2.imshow("median",median_B)
# cv2.imshow("median_O",img_duvar)
cv2.imshow("bilateral_O",img_duvar)
cv2.imshow("bilateral",bilateral)



cv2.waitKey(0)
cv2.destroyAllWindows()