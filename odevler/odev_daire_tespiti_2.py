import cv2
import numpy as np

img=cv2.imread("bozuk_paralar_2.jpg")
img=cv2.resize(img,(640,480))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,19)

circle=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/5,param1=180,param2=30,minRadius=20,maxRadius=400)

if circle is not None:
    circle=np.uint16(np.around(circle))
    for i in circle[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),3)

cv2.putText(img, f'{circle.shape[1]} tane daire var', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("bozuk_paralar",img)    # .shape[1] ===> sayıyı verir
# cv2.imshow("blur",blur)    
cv2.waitKey(0)
cv2.destroyAllWindows()