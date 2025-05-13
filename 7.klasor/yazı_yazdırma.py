import cv2
import numpy as np
canvas=np.zeros((512,512,3),np.uint8) + 255

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"sude",(20,40),font1,2,(255,255,100),2)
#tuval,yazılacak metin,başlangıç kordinantı,yazı şekli,kalınlık,renk,yazı tipi(varsayılan)=cv2.LINE_AA

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Boş bir resim oluştur
# img = np.zeros((400, 600, 3), dtype=np.uint8)

# # Yazıyı ekle
# cv2.putText(img, "sude", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# # Görüntüyü göster
# cv2.imshow('Yazi', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()