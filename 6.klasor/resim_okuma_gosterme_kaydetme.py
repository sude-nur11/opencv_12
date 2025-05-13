import cv2
# import numpy as np
# import matplotlib

img=cv2.imread("dunya-haritasi-2.jpg")

cv2.namedWindow("image",cv2.WINDOW_NORMAL)  # resmimizi anlık olrak boyutlandırabilmemizi sağlar

cv2.imshow("image",img)
# cv2.imwrite("dunya-haritasi-3",img)  # bu kısımdada resmi kaydeder
cv2.waitKey(0)  # 0 yazma nedenimiz biz herhangibir tuşa ya da pencereyi kaoatana kadar ekranda tutar
cv2.destroyAllWindows()  # pencereleri kapattıgımıza bütün pencerelerin kapandıgından emin olur      